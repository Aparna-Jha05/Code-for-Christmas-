import hashlib
import json

def compute_hash(wallet, score, bucket, explanation):
    payload = {
        "wallet": wallet,
        "score": score,
        "bucket": bucket,
        "explanation": explanation
    }
    raw = json.dumps(payload, sort_keys=True).encode()
    return hashlib.sha256(raw).hexdigest()
