from brownie import SimpleStorage, accounts

def test_deploy(): 
    #Arrange
    local_account = accounts[0]
    #Act
    simple_storage = SimpleStorage.deploy({"from": local_account})
    starting_value = simple_storage.getFavNo()
    expected = 5
    #Assert
    assert starting_value == expected
    
def test_update_storage(): 
    #Arrange
    local_account = accounts[0]
    #Act
    simple_storage = SimpleStorage.deploy({"from": local_account})
    transaction = simple_storage.storeFavNo(250, {"from": local_account})
    transaction.wait(1)
    updated_value = simple_storage.getFavNo()
    expected = 250
    #Assert
    assert updated_value == expected