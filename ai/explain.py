from ai.groq_client import get_groq_client

def generate_explanation(features: dict, score: float) -> dict:
    # Skip AI for low-risk wallets
    if score < 0.3:
        return {
            "explanation": "No significant Sybil behavior detected. Activity patterns appear independent and non-coordinated.",
            "confidence": "LOW"
        }

    # Determine dominant signal (deterministic)
    cts = features["creation_time_similarity"]
    txo = features["tx_pattern_overlap"]
    ent = features["interaction_entropy"]

    if cts >= txo and cts >= (1 - ent):
        dominant = "creation_time"
        reason = "wallets created in a tightly correlated time window"
    elif txo >= cts and txo >= (1 - ent):
        dominant = "transaction_overlap"
        reason = "highly overlapping transaction behavior"
    else:
        dominant = "entropy_collapse"
        reason = "low interaction entropy indicating scripted activity"

    prompt = f"""
You are a blockchain security analyst writing for protocol reviewers.

Context:
This wallet is flagged due to {reason}.

Signals:
- Creation time similarity: {cts}
- Transaction overlap: {txo}
- Interaction entropy: {ent}

Instructions:
- Explain the risk in concrete, technical terms.
- Tie the explanation directly to the dominant signal.
- Do NOT mention AI, models, or probabilities.
- Maximum 2 sentences.
- Neutral, audit-style language.
"""

    client = get_groq_client()

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,   # 🔑 lower = more deterministic
        max_tokens=70,
    )

    explanation = response.choices[0].message.content.strip()

    return {
        "explanation": explanation,
        "confidence": "HIGH" if score > 0.7 else "MEDIUM"
    }
