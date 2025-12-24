from ml.scorer import score_wallet

test_wallet_data = {
    "creation_time_similarity": 0.9,
    "tx_pattern_overlap": 0.85,
    "interaction_entropy": 0.2
}

result = score_wallet("0xA1", test_wallet_data)

print(result)
