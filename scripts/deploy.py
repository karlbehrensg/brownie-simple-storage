from brownie import accounts, config, SimpleStorage, network


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])


def deploy_simple_storage():
    # Account
    account = get_account()

    # Deploy contract
    simple_storage = SimpleStorage.deploy({"from": account})

    # Get stored value
    store_value = simple_storage.retrive()
    print(store_value)

    # Set new value
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)

    # Get new stored value
    updated_store_value = simple_storage.retrive()
    print(updated_store_value)


def main():
    deploy_simple_storage()
