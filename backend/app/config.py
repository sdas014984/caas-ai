import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")
TENANT_DIR = os.path.join(DATA_DIR, "tenants")

MODEL_NAME = os.getenv("MODEL_NAME", "llama3")
EMBEDDING_MODEL = "all-MiniLM-L6-v2"