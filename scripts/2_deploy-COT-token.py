from brownie import accounts, config, COTToken

#get parameters from constructor function
initial_supply = 1000000000000000000
token_name = "COTToken"
token_symbol = "COT"

def main():
    account = accounts[0]
    erc20 = COTToken.deploy(initial_supply,{"from": account}
    )