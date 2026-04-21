import sys
import os
from app.tenant import get_tenant_paths, ensure_tenant_dirs
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

def ingest(tenant_id: str):

    paths = ensure_tenant_dirs(tenant_id)

    docs = []
    for file in os.listdir(paths["docs"]):
        docs.extend(TextLoader(os.path.join(paths["docs"], file)).load())

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    db = Chroma.from_documents(
        chunks,
        embedding,
        persist_directory=paths["db"]
    )

    db.persist()

    print(f"✅ Ingested tenant: {tenant_id}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ingest.py <tenant_id>")
        sys.exit(1)

    ingest(sys.argv[1])