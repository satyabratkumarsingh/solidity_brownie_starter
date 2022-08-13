import imp
from os import access
from brownie import FundMe, network, config
from scripts.utils  import get_account, deploy_mocks_aggregator, LOCAL_BLOCKCHAIN_NETWORKS

def deploy_fund_me(): 
    account = get_account()
    if(network.show_active() not in LOCAL_BLOCKCHAIN_NETWORKS):
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        price_feed_address = deploy_mocks_aggregator()
        print("Deployed mocks")
       
    fund_me = FundMe.deploy(price_feed_address, {"from": account}, publish_source = config["networks"][network.show_active()]["verify"])
    print(f"Contract deployed to {fund_me.address}")
    return fund_me

def main():
    deploy_fund_me()