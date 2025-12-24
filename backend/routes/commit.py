from fastapi import APIRouter
from backend.services.trust_store import TRUST_STATE
from backend.config import w3, contract, ACCOUNT_ADDRESS, PRIVATE_KEY

router = APIRouter()

BUCKET_MAP = {
    "LOW": 0,
    "MEDIUM": 1,
    "HIGH": 2
}

@router.post("/commit")
def commit():
    receipts = []

    nonce = w3.eth.get_transaction_count(ACCOUNT_ADDRESS)

    for wallet, trust in TRUST_STATE.items():
        tx = contract.functions.commitTrust(
            w3.to_checksum_address(wallet),
            BUCKET_MAP[trust["bucket"]],
            bytes.fromhex(trust["hash"])
        ).build_transaction({
            "from": ACCOUNT_ADDRESS,
            "nonce": nonce,
            "gas": 300000,
            "gasPrice": w3.to_wei("20", "gwei")
        })

        signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

        receipts.append({
            "wallet": wallet,
            "tx_hash": tx_hash.hex()
        })

        nonce += 1

    return {
        "message": "Trust committed on-chain",
        "transactions": receipts
    }
