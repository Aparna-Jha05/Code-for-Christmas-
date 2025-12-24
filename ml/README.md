# ML – Sybil Probability Scoring

This module computes a **Sybil probability score** for wallets based on
simple, explainable behavioral features.

IMPORTANT:
- ML DOES NOT make decisions
- ML DOES NOT enforce anything
- ML ONLY outputs a probability (0–1)

---

## Files

### `feature_engineering.py`
Extracts normalized behavioral features for a wallet.

```python
extract_features(wallet_id: str, wallet_data: dict) -> dict
Expected feature keys (ALL REQUIRED):

creation_time_similarity (float, 0–1)

tx_pattern_overlap (float, 0–1)

interaction_entropy (float, 0–1)

sybil_model.py
Computes a deterministic Sybil probability score.

python
Copy code
compute_sybil_score(features: dict) -> float
Output:

Float between 0.0 and 1.0

No randomness. No learning. Fully explainable.

scorer.py ⭐ (MAIN ENTRY POINT)
THIS IS THE ONLY FUNCTION THE BACKEND SHOULD CALL.

python
Copy code
from ml.scorer import score_wallet

score_wallet(wallet_id: str, wallet_data: dict) -> dict
Returns:

json
Copy code
{
  "wallet": "0xA1",
  "sybil_probability": 0.87,
  "features": {
    "creation_time_similarity": 0.9,
    "tx_pattern_overlap": 0.85,
    "interaction_entropy": 0.2
  },
  "model_version": "sybil-linear-v1"
}
Guarantees
Deterministic output

Stable JSON schema

No external dependencies

Safe to call inside FastAPI routes

Do NOT Change
Function names

Returned JSON keys

Score range (must be 0–1)

Backend and demo scripts depend on this exact contract.