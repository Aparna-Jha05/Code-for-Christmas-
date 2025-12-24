# ml/scorer.py

from ml.feature_engineering import extract_features
from ml.sybil_model import compute_sybil_score

MODEL_VERSION = "sybil-linear-v1"

def score_wallet(wallet_id: str, wallet_data: dict) -> dict:
    features = extract_features(wallet_id, wallet_data)
    score = compute_sybil_score(features)

    return {
        "wallet": wallet_id,
        "sybil_probability": score,
        "features": features,
        "model_version": MODEL_VERSION
    }
