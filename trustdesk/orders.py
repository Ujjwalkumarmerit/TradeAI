from dataclasses import dataclass, asdict
import time
@dataclass
class Order:
    order_id:str; email:str; status:str; item:str; dispatched_at:str|None; tracking_status:str
ORDERS={
"ORD-1001":Order("ORD-1001","maya@example.com","in_transit","Wireless headphones","2026-11-08","At regional sorting facility"),
"ORD-1002":Order("ORD-1002","arjun@example.com","delivered","Desk lamp","2026-11-03","Delivered"),
"ORD-1003":Order("ORD-1003","sana@example.com","processing", "Coffee grinder",None,"Not dispatched")}
class OrderServiceError(Exception): pass
class OrderNotFound(OrderServiceError): pass
class OrderUnauthorized(OrderServiceError): pass
class OrderUnavailable(OrderServiceError): pass
class MockOrderService:
    """Replace this adapter with employer service; failures are deterministic for tests."""
    def __init__(self,delay=0.0,fail=False,malformed=False): self.delay,self.fail,self.malformed=delay,fail,malformed
    def lookup(self,order_id,email,timeout=1.0):
        if self.delay:
            if self.delay>timeout: raise OrderUnavailable("Order service timed out")
            time.sleep(self.delay)
        if self.fail: raise OrderUnavailable("Order service is temporarily unavailable")
        if self.malformed: raise OrderUnavailable("Order service returned malformed data")
        order=ORDERS.get(order_id)
        if not order: raise OrderNotFound("Order not found")
        if order.email.lower()!=email.lower(): raise OrderUnauthorized("Order identity could not be verified")
        return asdict(order)
