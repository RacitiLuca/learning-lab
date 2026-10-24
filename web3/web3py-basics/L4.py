from web3 import Web3
import json

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccount = web3.eth.accounts[0]

abi = json.loads('[{"constant": false, "inputs": [{"name": "_greeting", "type": "string"}], "name": "setGreeting", "outputs": [], "payable":false, "stateMutability":"nonpayable", "type":"function"}, {"constant": true, "inputs": [], "name":"greet", "outputs":[{"name": "", "type": "string"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [], "name":"greeting", "outputs":[{"name": "", "type": "string"}], "payable": false, "stateMutability": "view", "type": "function"}, {"inputs": [], "payable":false, "stateMutability":"nonpayable", "type":"constructor"}]')
address = Web3.toChecksumAddress("0xcD4c3EB9bbA5f4c010CeBDbc809f42763F274A7f")

contract = web3.eth.contract(address=address, abi=abi)

print(contract.functions.greet().call())

tx_hash = contract.functions.setGreeting('Thats the new Greeting!').transact()

# print(tx_hash)

print(web3.toHex(tx_hash))

web3.eth.waitForTransactionReceipt(tx_hash)

print('Updated Greeting: {}'.format(
    contract.functions.greet().call()
))
