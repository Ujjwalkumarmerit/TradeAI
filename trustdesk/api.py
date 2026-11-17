from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from .engine import SupportEngine

app = FastAPI(title="TrustDesk AI", version="1.0.0", description="Grounded customer support assistant with safe order lookup.")
engine = SupportEngine()
class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=2000)
    order_id: str | None = None
    email: str | None = None
@app.get("/health")
def health():
    return {"ok": True, "active_knowledge_chunks": len(engine.kb.chunks)}
@app.post("/chat")
def chat(req: ChatRequest):
    return engine.answer(req.message, req.order_id, req.email)
@app.get("/", response_class=HTMLResponse)
def home():
    return """<!doctype html><html><head><meta charset='utf-8'><title>TrustDesk AI</title><style>body{font:16px system-ui;background:#f4f6fa;margin:0;padding:40px;color:#172033}main{max-width:760px;margin:auto;background:white;padding:28px;border-radius:16px}textarea,input{width:100%;box-sizing:border-box;padding:12px;margin:8px 0}button{padding:12px 20px}pre{white-space:pre-wrap}</style></head><body><main><h1>TrustDesk AI</h1><p>Ask a policy question, or verify an order with its ID and checkout email.</p><textarea id='message' rows='4' placeholder='How long do approved refunds take?'></textarea><input id='order' placeholder='Order ID (optional)'><input id='email' placeholder='Checkout email (optional)'><button onclick='send()'>Ask TrustDesk</button><pre id='out'>Your grounded answer will appear here.</pre><script>async function send(){let out=document.getElementById('out');out.textContent='Checking...';try{let r=await fetch('/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:document.getElementById('message').value,order_id:document.getElementById('order').value||null,email:document.getElementById('email').value||null})});out.textContent=JSON.stringify(await r.json(),null,2)}catch(e){out.textContent='Request failed: '+e}}</script></main></body></html>"""
