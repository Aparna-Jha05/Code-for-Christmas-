import json

def load_demo_wallets():
    with open("data/demo_wallets.json") as f:
        data = json.load(f)

    wallets = []
    for group in data.values():
        wallets.extend(group)

    return wallets
