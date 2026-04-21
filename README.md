# Multi-Tenant GenAI CCaaS

## Features
- Multi-tenant RAG system
- API-key authentication
- ChromaDB per tenant
- Ollama LLM
- Twilio webhook support

## Setup

### 1. Start services
docker compose up -d

### 2. Create tenant
mkdir -p backend/data/tenants/tenantA/docs

### 3. Add docs
echo "Refund is 7 days" > backend/data/tenants/tenantA/docs/refund.txt

### 4. Ingest
python backend/app/ingest.py tenantA

### 5. Test
curl -X POST http://localhost:5000/chat \
-H "api-key: tenantA-key" \
-H "Content-Type: application/json" \
-d '{"message":"refund policy?"}'