# ml/sybil_model.py

def compute_sybil_score(features: dict) -> float:
    """
    Compute Sybil probability score between 0 and 1.
    """

    score = (
        0.4 * features["creation_time_similarity"] +
        0.5 * features["tx_pattern_overlap"] +
        0.1 * (1 - features["interaction_entropy"])
    )

    # Clamp for safety
    return round(min(max(score, 0.0), 1.0), 3)
