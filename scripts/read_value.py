from brownie import SimpleStorage, accounts, config


def read_contract():
    # Use -1 to get the last version of the contract
    simple_storage = SimpleStorage[-1]

    print(simple_storage.retrive())


def main():
    read_contract()
