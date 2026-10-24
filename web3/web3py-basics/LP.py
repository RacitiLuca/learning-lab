import os
from web3 import Web3
import json

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))


acc1 = "0x926546002a9cD1E1f23a049Bb7a09d2Bb4B468E5"
acc2 = "0x220f396460C12B35A1f29De2f3BBB88C8CDa9500"
acc3 = "0xFb2B4847D4634701087ceB73477d618935fd0b71"

private_key1 = os.getenv("PRIVATE_KEY_1", "")
private_key2 = os.getenv("PRIVATE_KEY_2", "")
private_key3 = os.getenv("PRIVATE_KEY_3", "")

nonce1 = web3.eth.get_transaction_count(acc1)
nonce2 = web3.eth.get_transaction_count(acc2)
nonce3 = web3.eth.get_transaction_count(acc3)


tx1 = {
    'nonce': nonce1,
    'to': acc2,
    'value': web3.toWei(10, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

tx2 = {
    'nonce': nonce2,
    'to': acc3,
    'value': web3.toWei(15, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

tx3 = {
    'nonce': nonce3,
    'to': acc1,
    'value': web3.toWei(20, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

signed_tx1 = web3.eth.account.signTransaction(tx1, private_key1)
signed_tx2 = web3.eth.account.signTransaction(tx2, private_key2)
signed_tx3 = web3.eth.account.signTransaction(tx3, private_key3)

tx_hash1 = web3.eth.sendRawTransaction(signed_tx1.rawTransaction)
tx_hash2 = web3.eth.sendRawTransaction(signed_tx2.rawTransaction)
tx_hash3 = web3.eth.sendRawTransaction(signed_tx3.rawTransaction)


print(Web3.toHex(tx_hash1))
print(Web3.toHex(tx_hash2))
print(Web3.toHex(tx_hash3))
