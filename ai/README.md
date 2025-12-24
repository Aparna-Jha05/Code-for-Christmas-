# 📁 `ai/README.md`

```md
# AI – Explanation Layer (Groq)

This module generates **human-readable explanations** for Sybil behavior.
It DOES NOT affect scoring or enforcement.

AI is used ONLY for interpretability.

---

## Model Used

Groq model:
llama-3.1-8b-instant

yaml
Copy code

Why:
- Fast
- Cheap
- Deterministic enough for demos
- Replaceable without affecting logic

---

## Environment Setup

AI requires a Groq API key.

Create a `.env` file at PROJECT ROOT:

```env
GROQ_API_KEY=your_api_key_here
DO NOT commit .env.

Files
groq_client.py
Initializes Groq client once and reuses it.

python
Copy code
get_groq_client() -> Groq
Loads API key via python-dotenv

Throws error if key is missing

explain.py ⭐ (MAIN ENTRY POINT)
THIS IS THE ONLY FUNCTION THE BACKEND SHOULD CALL.

python
Copy code
from ai.explain import generate_explanation

generate_explanation(features: dict, score: float) -> dict
Behavior:

If score < 0.3 → no Groq call (skipped)

Otherwise → one Groq call

Returns:

json
Copy code
{
  "explanation": "Human-readable explanation text",
  "confidence": "LOW | MEDIUM | HIGH"
}
Prompt Rules
Max 2 sentences

Neutral, technical tone

No mention of AI, LLMs, or models

Guarantees
AI NEVER changes scores

AI NEVER decides enforcement

Output format is stable

Safe for FastAPI usage

Do NOT Change
Function name: generate_explanation

Output keys: explanation, confidence

Temperature (>0.2 is not allowed)

Max tokens (>100 is not allowed)

Backend logic depends on this contract.

yaml
Copy code

---

## WHAT YOUR FRIEND NEEDS TO KNOW (TL;DR FOR THEM)

Tell your teammate **this exact summary**:

> “Call `score_wallet()` from ML, then pass its `features` and `sybil_probability` into `generate_explanation()`.  
> Do not modify outputs. Enforcement logic is yours.”

That’s it.

---
