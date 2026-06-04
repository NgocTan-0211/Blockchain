from web3 import Web3
import json

GANACHE_URL = "http://127.0.0.1:7545"

web3 = Web3(
    Web3.HTTPProvider(
        GANACHE_URL
    )
)

with open(
    "blockchain/abi.json"
) as f:

    abi = json.load(f)

CONTRACT_ADDRESS = "YOUR_CONTRACT_ADDRESS"

contract = web3.eth.contract(
    address=CONTRACT_ADDRESS,
    abi=abi
)

def save_hash(hash_value):

    tx = contract.functions.addEvent(
        hash_value
    ).transact(
        {
            "from":
            web3.eth.accounts[0]
        }
    )

    receipt = web3.eth.wait_for_transaction_receipt(tx)

    return receipt.transactionHash.hex()