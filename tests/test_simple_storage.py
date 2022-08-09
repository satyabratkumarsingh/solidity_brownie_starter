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