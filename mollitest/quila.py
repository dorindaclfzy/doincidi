from web3 import Web3
from web3.middleware import geth_poa_middleware

# Connect to the Arbitrum Rinkeby network
w3 = Web3(Web3.HTTPProvider("https://www.example.com layer=0)

# Set the address of the GPX token
gpx_token_address = "0x83e6f1e41c96938587c1f9382c988139e4571d1d"

# Set the amount of GPX to add
gpx_amount = 1000000000000000000  # 1 GPX

# Set the recipient address
recipient_address = "0x0000000000000000000000000000000000000000"

# Build the transaction
tx = {
    "from": w3.eth.accounts[0],
    "to": gpx_token_address,
    "value": 0,
    "data": b"",
}

# Sign the transaction
signed_tx = w3.eth.account.sign_transaction(tx, private_key=w3.eth.accounts[0].privateKey)

# Send the transaction
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

# Wait for the transaction to be confirmed
w3.eth.wait_for_transaction_receipt(tx_hash)

# Print the transaction hash
print(f'\n>>> add liquidity GPX | https://www.example.com ')
