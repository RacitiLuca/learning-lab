import os
from web3 import Web3


infura_url = os.getenv("INFURA_URL", "https://mainnet.infura.io/v3/<YOUR_PROJECT_ID>")
web3 = Web3(Web3.HTTPProvider(infura_url))


print(web3.eth.blockNumber)

latest = web3.eth.blockNumber
print(latest)
print(web3.eth.getBlock(latest))

for i in range(0, 10):
    print(web3.eth.getBlock(latest - i))

hash = '0x1ba93d172f68a47d6e64b7e33858fb646052680567bfcf96690dd73195223fd8'
print(web3.eth.getTransactionByBlock(hash, 2))


print(web3.toWei(13800968, 'ether'))
