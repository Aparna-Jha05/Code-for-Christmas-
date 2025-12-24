from fastapi import APIRouter
from backend.services.policy_engine import bucketize
from backend.services.hash_utils import compute_hash
from backend.services.trust_store import TRUST_STATE
from backend.services.data_loader import load_demo_wallets

from ml.scorer import score_wallet
from ai.explain import generate_explanation

router = APIRouter()

@router.post("/analyze")
def analyze(payload: dict | None = None):
    """
    Analyze wallets and write trust memory.
    If payload contains wallets -> use them.
    Otherwise -> load demo wallets.
    """

    # 🔹 Source of wallets
    if payload and "wallets" in payload:
        wallets = payload["wallets"]
    else:
        wallets = load_demo_wallets()

    results = []

    for wallet_id in wallets:
        # 🔹 Simulated behavioral signals (demo-only)
        if wallet_id.startswith("0xN"):  # normal users
            wallet_data = {
                "creation_time_similarity": 0.2,
                "tx_pattern_overlap": 0.3,
                "interaction_entropy": 0.8,
            }
        elif wallet_id.startswith("0xB"):  # borderline users
            wallet_data = {
                "creation_time_similarity": 0.5,
                "tx_pattern_overlap": 0.5,
                "interaction_entropy": 0.5,
            }
        else:  # sybil clusters
            wallet_data = {
                "creation_time_similarity": 0.8,
                "tx_pattern_overlap": 0.7,
                "interaction_entropy": 0.2,
            }

        # 1️⃣ ML scoring
        ml_result = score_wallet(wallet_id, wallet_data)
        score = ml_result["sybil_probability"]
        features = ml_result["features"]

        # 2️⃣ Deterministic policy
        bucket = bucketize(score)

        # 3️⃣ AI explanation (non-authoritative)
        ai_result = generate_explanation(features, score)

        # 4️⃣ Hash commitment (on-chain ready)
        analysis_hash = compute_hash(
            wallet_id,
            score,
            bucket,
            ai_result["explanation"]
        )

        # 5️⃣ WRITE TRUST MEMORY (single source of truth)
        TRUST_STATE[wallet_id] = {
            "bucket": bucket,
            "score": score,
            "hash": analysis_hash
        }

        results.append({
            "wallet": wallet_id,
            "sybil_score": score,
            "bucket": bucket,
            "explanation": ai_result["explanation"],
            "confidence": ai_result["confidence"],
            "model_version": ml_result["model_version"],
            "hash": analysis_hash
        })

    return {
        "mode": "demo-batch-analysis",
        "wallets_analyzed": len(results),
        "results": results
    }
