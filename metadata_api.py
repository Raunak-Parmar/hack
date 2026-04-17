from fastapi import APIRouter
from backend.models.requests import MetadataRequest
from backend.services.metadata_service import collect_metadata

router = APIRouter(prefix="/collect-metadata", tags=["Metadata"])

@router.get("")
def health():
    return {"status": "ok"}

@router.post("/")
def collect(payload: MetadataRequest):
    try:
        print("📥 Received metadata request:", payload.dict())

        result = collect_metadata(payload)

        return {
            "status": "success",
            "data": result
        }

    except Exception as e:
        # ✅ NEVER let FastAPI exit without returning a response
        print("❌ Metadata collection failed:", repr(e))

        return {
                    "status": "error",
                                "message": str(e)
                                        }
