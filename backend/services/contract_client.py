import json
from web3 import Web3
from backend.config import CONTRACT_ADDRESS, RPC_URL, PRIVATE_KEY

w3 = Web3(Web3.HTTPProvider(RPC_URL))
account = w3.eth.account.from_key(PRIVATE_KEY)

with open("blockchain/contracts/TrustRegistry.json") as f:
    abi = json.load(f)["abi"]

contract = w3.eth.contract(
    address=Web3.to_checksum_address(CONTRACT_ADDRESS),
    abi=abi
)

def commit_trust_onchain(wallet: str, bucket: int, analysis_hash: str):
    nonce = w3.eth.get_transaction_count(account.address)

    tx = contract.functions.commitTrust(
        Web3.to_checksum_address(wallet),
        bucket,
        bytes.fromhex(analysis_hash[2:])
    ).build_transaction({
        "from": account.address,
        "nonce": nonce,
        "gas": 300000,
        "gasPrice": w3.to_wei("1", "gwei")
    })

    signed_tx = account.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    return tx_hash.hex()
