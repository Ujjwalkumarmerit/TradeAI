from .knowledge import KnowledgeBase
from .orders import MockOrderService, OrderNotFound, OrderUnauthorized, OrderUnavailable
from .generation import GroundedGenerator

HIGH_RISK=("chargeback","lawsuit","legal action","sue you","fraud","account takeover","suicide","hurt myself","threat","medical emergency")
INJECTION=("ignore previous instructions","reveal system prompt","show internal notes","bypass policy","act as system","developer message")
class SupportEngine:
    def __init__(self,kb=None,orders=None,threshold=0.18,generator=None):
        self.kb=kb or KnowledgeBase(); self.orders=orders or MockOrderService(); self.threshold=threshold
        self.generator=generator or GroundedGenerator()
    def answer(self,message,order_id=None,email=None):
        msg=(message or "").strip()
        if not msg: return self._handoff("Please enter a question.","empty_message")
        lower=msg.lower()
        if any(t in lower for t in HIGH_RISK):
            return self._handoff("This needs a trained support specialist. I will not make a decision about this here.","high_risk")
        if any(t in lower for t in INJECTION):
            return self._handoff("I can help with customer-facing policies, but I cannot reveal internal instructions or notes.","prompt_injection")
        if any(t in lower for t in ("customs duties","customs fees","customs charges","customs clearance","import duties")):
            return self._handoff("The available policy explicitly does not specify customs charges or clearance timing. A human agent must confirm this.","knowledge_gap")
        phrases=("where is my order","track my order","order status","has my order shipped","delivery status","order is delayed","my order is delayed","order is late","my order is late","delivery is delayed","delivery delayed","package is delayed","package delayed","hasn't arrived","has not arrived")
        intent=any(p in lower for p in phrases) or ("order" in lower and any(t in lower for t in ("delayed","late","not arrived")))
        if intent:
            if not order_id or not email: return self._handoff("To check an order, provide the order ID and the email address used at checkout.","missing_order_identity")
            try:
                o=self.orders.lookup(order_id,email)
                return {"status":"answered","answer":f"Order {o['order_id']} is currently {o['status'].replace('_',' ')}. Item: {o['item']}. Latest tracking status: {o['tracking_status']}.","citations":[{"source":"Mock Order Service","id":"ORDER-LOOKUP"}],"order":{k:v for k,v in o.items() if k!="email"},"reason":"Verified order-service response"}
            except OrderUnauthorized:
                return self._handoff("I could not verify that order with the supplied details. Please check them or contact a support specialist.","order_identity_mismatch")
            except OrderNotFound:
                return self._handoff("I could not find that order. Please check the order ID or contact support.","order_not_found")
            except OrderUnavailable:
                return self._handoff("The order service is unavailable right now. I have not guessed at your order status; please try again or contact support.","order_service_error")
        results=self.kb.search(msg)
        if not results or results[0]["score"]<self.threshold or results[0]["matches"]<2:
            return self._handoff("I cannot find reliable support information for that question. A human agent should confirm it.","insufficient_evidence")
        cites=[{"id":r["doc_id"],"title":r["title"],"excerpt":r["text"],"updated_at":r["updated_at"]} for r in results[:2] if r["score"]>=self.threshold]
        generated=self.generator.generate(msg,results[:2]) if self.generator else None
        return {"status":"answered","answer":generated or results[0]["text"],"citations":cites,"reason":f"Retrieved evidence score {results[0]['score']:.3f}"+("; LLM-assisted" if generated else "; extractive safe fallback")}
    @staticmethod
    def _handoff(message,reason):
        return {"status":"escalated","answer":message,"citations":[],"escalation_reason":reason,"handoff":"A human support agent should review this request."}
