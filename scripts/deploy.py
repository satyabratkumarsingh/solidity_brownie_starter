from brownie  import accounts, config, SimpleStorage


def deploy_simple_storage():
    account= accounts.load("testaccount")
    pvt_key = config["wallets"]["from_key"]
    print('@@@@@@@ PVT KEY @@@@@@@')
    print(pvt_key)
    print(account)
    local_account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": local_account})
    transaction = simple_storage.storeFavNo(250, {"from": local_account})
    transaction.wait(1)
    updated_value = str(simple_storage.getFavNo())
    print("The Fav No is " + updated_value)

def main():
    deploy_simple_storage()