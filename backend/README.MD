# 📁 Backend – Airdrop Trust Protocol

This backend is the **single source of truth** for the entire system.

## It Orchestrates:
- ML scoring
- AI explanations
- Deterministic policy enforcement
- Airdrop allocation

**Frontend, ML, and AI NEVER enforce logic.**

---

## Tech Stack

- Python 3.12
- FastAPI
- Uvicorn
- Modular architecture

---

## How to Run

From **PROJECT ROOT**:
```bash
uvicorn backend.main:app --reload
```

Open API docs: `http://127.0.0.1:8000/docs`

---

## Folder Structure
```
backend/
├── main.py
├── routes/
│   ├── analyze.py
│   ├── airdrop.py
│   └── commit.py          (optional / future)
├── services/
│   ├── policy_engine.py
│   ├── hash_utils.py
│   └── config.py
└── README.md
```

---

## main.py

### Purpose
- Initialize FastAPI app
- Configure CORS
- Mount all routes

### Mounted Routes
- `/analyze`
- `/airdrop`

**No logic lives here.**

---

## Route: POST /analyze

### File
`backend/routes/analyze.py`

### Purpose
Run the full trust analysis pipeline.

### Input
```json
{
  "wallets": ["0xA1", "0xA2", "0xB1"]
}
```

### Internal Flow (IMPORTANT)

#### 1. Mock wallet_data
- Temporary for demo
- Later replaced by indexer

#### 2. ML Scoring
```python
score_wallet(wallet_id, wallet_data)
```
**Returns:**
- `sybil_probability`
- `features`
- `model_version`

#### 3. Policy Engine
```python
bucketize(score)
```
**Buckets:**
- `LOW` (< 0.3)
- `MEDIUM` (< 0.7)
- `HIGH` (>= 0.7)

#### 4. AI Explanation
```python
generate_explanation(features, score)
```
**AI is interpretive ONLY.**

#### 5. Hash Commitment
```python
compute_hash(wallet, score, bucket, explanation)
```

### Output
```json
[
  {
    "wallet": "0xA1",
    "sybil_score": 0.75,
    "bucket": "HIGH",
    "explanation": "...",
    "confidence": "HIGH",
    "model_version": "sybil-linear-v1",
    "hash": "abc123"
  }
]
```

---

## Route: GET /airdrop

### File
`backend/routes/airdrop.py`

### Purpose
Apply trust-weighted reward distribution.

### Current Logic (Demo)
- `LOW` risk → high reward
- `MEDIUM` risk → medium reward
- `HIGH` risk → minimal reward

### Output Shape (IMPORTANT)
```json
{
  "mode": "trust-weighted-airdrop",
  "results": [
    { "wallet": "0xA1", "tokens": 100 },
    { "wallet": "0xA2", "tokens": 10 },
    { "wallet": "0xB1", "tokens": 50 }
  ]
}
```

**Frontend depends on:**
- `results` being an array
- Keys: `wallet`, `tokens`

---

## services/policy_engine.py

### Purpose
Deterministic enforcement.

### Logic
```python
if score < 0.3:
    LOW
elif score < 0.7:
    MEDIUM
else:
    HIGH
```

**NO AI here.**  
**NO randomness.**  
**NO side effects.**

---

## services/hash_utils.py

### Purpose
Generate deterministic hash for:
- score
- bucket
- explanation

### Used later for:
- On-chain commitment
- Dispute resolution

---

## ML & AI Integration Rules (CRITICAL)

### Backend may call ONLY:
```python
from ml.scorer import score_wallet
from ai.explain import generate_explanation
```

### Backend MUST NOT:
- Modify ML outputs
- Influence AI prompts
- Use AI for enforcement

---

## Import Rules (VERY IMPORTANT)

Because server is run as:
```bash
uvicorn backend.main:app
```

### Imports MUST follow:
- `backend.services.*`
- `backend.routes.*`
- `ml.*`
- `ai.*`

**Never use relative imports.**

---

## Design Philosophy

- **ML** = signal
- **AI** = interpretation
- **Backend** = authority
- **Frontend** = visualization
- **Blockchain** (future) = memory

---

## One-Sentence Summary

This backend is the **only place** where trust decisions are made.  
Everything else just assists or displays.