import os
from app.config import TENANT_DIR

def get_tenant_paths(tenant_id: str):
    base = os.path.join(TENANT_DIR, tenant_id)

    return {
        "docs": os.path.join(base, "docs"),
        "db": os.path.join(base, "chroma_db")
    }

def ensure_tenant_dirs(tenant_id: str):
    paths = get_tenant_paths(tenant_id)

    os.makedirs(paths["docs"], exist_ok=True)
    os.makedirs(paths["db"], exist_ok=True)

    return paths