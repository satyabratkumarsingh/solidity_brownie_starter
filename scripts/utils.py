import imp
from brownie import accounts, network, config, MockV3Aggregator
from web3 import Web3

DECIMALS = 18
STARTING_PRICE = 2000
LOCAL_BLOCKCHAIN_NETWORKS = ["development", "ganache-local"]

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_NETWORKS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
    
def deploy_mocks_aggregator():
    if(len(MockV3Aggregator) <=0):
        mock_agg = MockV3Aggregator.deploy(DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()})
    else:
        mock_agg = MockV3Aggregator[-1].address
    return mock_agg