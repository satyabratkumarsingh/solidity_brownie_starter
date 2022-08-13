from brownie  import accounts, config, SimpleStorage, network
from scripts.utils import get_account

def deploy_simple_storage():
    account= get_account()
    pvt_key = config["wallets"]["from_key"]
    print('@@@@@@@ PVT KEY @@@@@@@')
    print(pvt_key)
    print(account)
    #local_account = accounts[0]
    simple_storage_transaction = SimpleStorage.deploy({"from": account})
    transaction = simple_storage_transaction.storeFavNo(250, {"from": account})
    transaction.wait(1)
    updated_value = str(simple_storage_transaction.getFavNo())
    print("The Fav No is " + updated_value)
    
def main():
    deploy_simple_storage()