import os
from app.tenant import get_tenant_paths
from app.config import MODEL_NAME, EMBEDDING_MODEL
from app.prompts import SYSTEM_PROMPT

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

def get_rag_chain(tenant_id: str):

    paths = get_tenant_paths(tenant_id)

    if not os.path.exists(paths["db"]):
        raise Exception(f"Run ingestion first for tenant: {tenant_id}")

    embedding = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    db = Chroma(
        persist_directory=paths["db"],
        embedding_function=embedding
    )

    llm = Ollama(model=MODEL_NAME)

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=db.as_retriever(search_kwargs={"k": 3}),
        chain_type_kwargs={"prompt": SYSTEM_PROMPT}
    )

    return qa