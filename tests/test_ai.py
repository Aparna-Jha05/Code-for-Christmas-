from ai.explain import generate_explanation

features = {
    "creation_time_similarity": 0.9,
    "tx_pattern_overlap": 0.85,
    "interaction_entropy": 0.2
}

result = generate_explanation(features, score=0.87)
print(result)
