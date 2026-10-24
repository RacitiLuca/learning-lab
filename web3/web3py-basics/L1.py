import os
from web3 import Web3

infura_url = os.getenv("INFURA_URL", "https://mainnet.infura.io/v3/<YOUR_PROJECT_ID>")
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())

print(web3.eth.blockNumber)

balance = web3.eth.getBalance("0x3ef6fc394F6fA6657b7168595c26Aa6F330793Ba")
print(web3.fromWei(balance, "ether"))
