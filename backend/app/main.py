from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from pydantic import BaseModel

from app.auth import get_tenant
from app.rag import get_rag_chain
from app.utils import logger

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat")
def chat(req: ChatRequest, tenant_id: str = Depends(get_tenant)):
    logger.info(f"{tenant_id} -> {req.message}")

    qa = get_rag_chain(tenant_id)
    reply = qa.run(req.message)

    return {"tenant": tenant_id, "reply": reply}

@app.post("/twilio")
async def twilio(request: Request, tenant_id: str = Depends(get_tenant)):
    form = await request.form()
    message = form.get("Body")

    qa = get_rag_chain(tenant_id)
    reply = qa.run(message)

    return Response(
        content=f"<Response><Message>{reply}</Message></Response>",
        media_type="application/xml"
    )