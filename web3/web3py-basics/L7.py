import os
from web3 import Web3

infura_url = os.getenv("INFURA_URL", "https://mainnet.infura.io/v3/<YOUR_PROJECT_ID>")
web3 = Web3(Web3.HTTPProvider(infura_url))

acc = web3.eth.account.create()

print(acc.address)
print(acc.privateKey)

keystore = acc.encrypt('blabla')

print(keystore)

print(web3.eth.account.decrypt(keystore, 'blabla'))
