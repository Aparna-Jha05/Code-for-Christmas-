# ml/feature_engineering.py

def extract_features(wallet_id: str, wallet_data: dict) -> dict:
    """
    Extract explainable Sybil-related features for a wallet.
    All values must be normalized between 0 and 1.
    """

    # These are MOCKED / SIMULATED for MVP
    # Later can be replaced with real indexer output

    features = {
        "creation_time_similarity": wallet_data.get("creation_time_similarity", 0.0),
        "tx_pattern_overlap": wallet_data.get("tx_pattern_overlap", 0.0),
        "interaction_entropy": wallet_data.get("interaction_entropy", 1.0),
    }

    return features
