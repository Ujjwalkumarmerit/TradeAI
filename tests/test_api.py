from fastapi.testclient import TestClient
from trustdesk.api import app
client=TestClient(app)
def test_health(): assert client.get("/health").json()["ok"] is True
def test_chat_validation(): assert client.post("/chat",json={"message":""}).status_code==422
def test_chat_answer():
    r=client.post("/chat",json={"message":"How long do approved refunds take?"})
    assert r.status_code==200 and r.json()["status"]=="answered"
