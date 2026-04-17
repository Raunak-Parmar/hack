# backend/api/reconciliation_api.py

from fastapi import APIRouter
from backend.models.requests import ReconciliationRequest
from backend.services.reconciliation_service import run_reconciliation_checks

router = APIRouter(prefix="/reconciliation", tags=["Reconciliation"])

@router.post("")   
def run_recon(payload: ReconciliationRequest):
    results = run_reconciliation_checks(payload)
    return {"status": "success", "results": results}
