from fastapi import Header, HTTPException

# Simulated API keys (store in DB in real system)
TENANTS = {
    "tenantA-key": "tenantA",
    "tenantB-key": "tenantB"
}

def get_tenant(api_key: str = Header(...)):
    if api_key not in TENANTS:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return TENANTS[api_key]
