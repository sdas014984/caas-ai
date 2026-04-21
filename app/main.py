from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.rag import get_rag_chain

app = FastAPI()
qa = get_rag_chain()

class ChatRequest(BaseModel):
    message: str
    channel: str = "chat"

@app.post("/chat")
def chat(req: ChatRequest):
    response = qa.run(req.message)
    return {"reply": response}

# Simulated Twilio webhook
@app.post("/twilio")
async def twilio_webhook(request: Request):
    form = await request.form()
    message = form.get("Body")

    reply = qa.run(message)

    return f"""
    <Response>
        <Message>{reply}</Message>
    </Response>
    """
