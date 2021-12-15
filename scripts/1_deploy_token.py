from brownie import accounts, config, TokenERC20

#get parameters from constructor function
initial_supply = 1000000000000000000
token_name = "come-on token"
token_symbol = "COT"

def main():
    account = accounts.add(config["wallets"]["from_key"])
    erc20 = TokenERC20.deploy(
        initial_supply,token_name,token_symbol, {"from": account}, publish_source=True
    )