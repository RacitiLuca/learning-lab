import os
from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# print(web3.eth.blockNumber)

acc1 = "0x0D521f69926E4B2Ed129512E32Ae8fD483c757f6"
acc2 = "0xD59B22609a57580cc7600896f83AF41304C0E577"

private_key1 = os.getenv("PRIVATE_KEY_1", "")
private_key2 = os.getenv("PRIVATE_KEY_2", "")

# get the nonce
nonce = web3.eth.get_transaction_count(acc1)

# build a transaction
tx = {
    'nonce': nonce,
    'to': acc2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

# sign transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key1)

# send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

# get transaction hash
print(tx_hash)

# get transioction hash in readable format
print(web3.toHex(tx_hash))
