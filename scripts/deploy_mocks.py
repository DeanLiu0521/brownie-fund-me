from brownie import network, MockV3Aggregator
from scripts.helpful_scripts import get_account

DECIMALS = 8
STARTING_PRICE = 200000000000


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print("Mocks Deployed!")
