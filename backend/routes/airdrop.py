from fastapi import APIRouter
from backend.services.trust_store import TRUST_STATE

router = APIRouter()

BASE_AIRDROP = 100

BUCKET_WEIGHTS = {
    "LOW": 1.0,
    "MEDIUM": 0.5,
    "HIGH": 0.1
}

@router.get("/airdrop")
def airdrop():
    result = []

    for wallet, trust in TRUST_STATE.items():
        bucket = trust["bucket"]
        weight = BUCKET_WEIGHTS[bucket]

        tokens = int(BASE_AIRDROP * weight)

        result.append({
            "wallet": wallet,
            "bucket": bucket,
            "tokens": tokens
        })

    return {
        "mode": "trust-weighted-airdrop",
        "results": result
    }
