from brownie  import accounts
import os

def deploy_simple_storage():
    account= accounts.load("testaccount")
    pvt_key = os.getenv("PRIVATE_KEY")
    print('@@@@@@@ PVT KEY @@@@@@@')
    print(pvt_key)
    print(account)

def main():
    deploy_simple_storage()