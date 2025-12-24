# AIRDROP-TRUST-PROTOCOL 😎

> Open Terminal (1)
``` 
git clone https://github.com/AbhishekYadav65/airdrop_trust_protocol 

pip install -r requirements.txt
```
```
cd blockchain
npm install
npx hardhat node
```
> Open Terminal (2)
```
uvicorn backend.main:app --reload 
```
> Open Terminal (3)
```
cd frontend
python -m http.server 5500
```

### Then click on 
<a href="
http://localhost:5500/">
Landing Page</a>




# Airdrop Trust Protocol

**Sybil-Resistant, Trust-Weighted Airdrops using Off-Chain Intelligence & Deterministic Enforcement**

---

## 1. One-Line Problem Statement 

Airdrops fail because decentralized systems cannot distinguish humans from Sybil farms — and current solutions either trust black-box AI or central authorities.

---

## 2. Core Insight (WHY THIS PROJECT EXISTS)

Blockchain systems face a native contradiction:

**On-chain logic must be:**
- deterministic
- verifiable
- cheap

**But Sybil detection requires:**
- behavioral analysis
- pattern recognition
- probabilistic reasoning

👉 Running ML or AI on-chain is infeasible and unsafe  
👉 Trusting AI blindly off-chain breaks decentralization

**Our insight:**

> ML should suggest, AI should explain — but only deterministic logic should enforce.

This project is built entirely around that separation.

---

## 3. High-Level Solution Overview

We built a Sybil-resistant airdrop mechanism where:

- ML computes a Sybil probability
- AI generates a human-readable explanation
- Backend applies strict, deterministic policy
- Airdrop rewards are trust-weighted
- Outputs are hash-committed for on-chain use

**No component has unchecked authority.**

---

## 4. Architecture Diagram (CORE OF THE PITCH)
```
┌────────────────────┐
│    Frontend UI     │
│ (Visualization)    │
│                    │
│ - Wallet input     │
│ - Results tables   │
└─────────┬──────────┘
          │ HTTP (REST)
          ▼
┌──────────────────────────────────┐
│        Backend (FastAPI)          │
│  SINGLE SOURCE OF TRUTH           │
│                                  │
│  1. Orchestrates pipeline         │
│  2. Enforces deterministic rules │
│  3. Controls all authority        │
└─────────┬──────────┬─────────────┘
          │          │
          │          │
          ▼          ▼
┌──────────────┐   ┌────────────────┐
│  ML Module   │   │   AI Module    │
│ (Sybil Score)│   │ (Explanation)  │
│              │   │                │
│ - Determin.  │   │ - Human-read.  │
│ - Probabil.  │   │ - Non-binding  │
│ - Explain.   │   │ - Skippable    │
└──────┬───────┘   └──────┬─────────┘
       │                  │
       └───────┬──────────┘
               ▼
     ┌──────────────────────┐
     │ Policy Engine        │
     │ (Deterministic)      │
     │                      │
     │ - Bucketize risk     │
     │ - Enforce rewards    │
     └─────────┬────────────┘
               ▼
     ┌──────────────────────┐
     │ Trust-Weighted       │
     │ Airdrop Allocation   │
     │                      │
     │ (On-chain ready)     │
     └──────────────────────┘
```

---

## 5. Frontend 
### Purpose
- Transparent visualization only
- Zero authority
- No hidden logic

### What it shows
- Wallet list
- Sybil score
- Risk bucket
- AI explanation
- Final token allocation

### Why it matters
Judges can visually verify that:
- AI explanations do not change outcomes
- Enforcement is rule-based
- High-risk wallets are penalized

**Frontend proves system integrity, not UX polish.**

---

## 6. Backend (The Brain)

### Role
The backend is the only authority in the system.

### Responsibilities
- Orchestrate ML + AI
- Apply deterministic policy
- Allocate rewards
- Prepare hash commitments for blockchain

### Key design choice
No randomness, no learning, no AI inside enforcement logic.

This ensures:
- replayability
- auditability
- governance compatibility

---

## 7. ML Module (Signal Generator)

### What it does
Computes a Sybil probability (0–1) using explainable features:
- creation-time similarity
- transaction overlap
- interaction entropy

### What it does NOT do
- No decisions
- No enforcement
- No randomness


This respects blockchain constraints:
- probabilistic insight stays off-chain
- results are explainable and reproducible

---

## 8. AI Module (Interpreter, Not Authority)

### Role
- Convert numeric signals into human-readable explanations
- Help developers, auditors, and DAOs understand why a wallet is risky

### Critical constraint
AI output is never trusted. It is only hashed and stored.

**If AI fails or lies:**
- system still behaves correctly

This avoids:
- oracle problems
- black-box governance
- AI centralization

---

## 9. Policy Engine (Key Innovation)

### Deterministic Rules
```
Sybil Score < 0.3  → LOW risk
Sybil Score < 0.7  → MEDIUM risk
Sybil Score ≥ 0.7  → HIGH risk
```

### Why this matters
- Anyone can recompute outcomes
- DAO governance can change thresholds
- No "AI decided" ambiguity

**This is where decentralized stability is enforced.**

---

## 10. Blockchain Component (Current + Future)

### Current State
Backend generates hash commitments of:
- score
- bucket
- explanation

### On-Chain Ready Design
These hashes can be:
- stored in a smart contract
- used for:
  - dispute resolution
  - audits
  - slashing
  - governance challenges

### Why this fits blockchain innovation
Blockchain is used as memory and enforcement, not computation.

---

## 11. Why This Is Open Innovation (Not Just an App)

This project does not just "use blockchain".

It solves a blockchain-native problem:
- Sybil resistance
- trust without identity
- probabilistic off-chain intelligence
- deterministic on-chain enforcement

**Web2 systems cannot do this without trusted intermediaries.**

---

## 12. Demo Flow 

1. Input wallets
2. Run analysis
3. Observe:
   - same wallets → same scores
   - AI explanations ≠ enforcement
4. Run airdrop
5. See:
   - honest wallets rewarded
   - Sybils throttled

👉 **No magic. No randomness. Fully reproducible.**

---

## 13. One-Sentence Closing

We built a system where intelligence informs decisions, but trust is enforced deterministically — making Sybil-resistant airdrops possible without central authority.
