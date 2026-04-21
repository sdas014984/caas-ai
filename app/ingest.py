import os
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

def ingest():
    docs = []
    for file in os.listdir("data/docs"):
        docs.extend(TextLoader(f"data/docs/{file}").load())

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    db = Chroma.from_documents(
        chunks,
        embedding,
        persist_directory="data/chroma_db"
    )

    db.persist()

if __name__ == "__main__":
    ingest()
