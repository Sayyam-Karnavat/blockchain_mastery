from algosdk.v2client.algod import AlgodClient
from algosdk import account , mnemonic , transaction
import pprint
import time

'''
Asset Configuration Transactions 

 1. Creating an ASA
    An ASA can represent anything from a cryptocurrency to a digital token. When creating an asset on Algorand, you can define attributes such as the total supply, decimals, asset name, and metadata.

    

Step-by-Step Code for Creating an ASA

    Transaction Parameters: Get the latest transaction parameters.(Suggested params)
    Define Asset Attributes: Define attributes such as total supply, decimals, and other metadata.
    Sign the Transaction: Sign the asset creation transaction with the creator's private key.
    Send the Transaction: Send the transaction to the Algorand network.
    Confirm the Transaction: Wait for the transaction to be confirmed.

'''
owner_mnemonic = "toss transfer sure frozen real jungle mouse inch smoke derive floor alter ten eagle narrow perfect soap weapon payment chaos amateur height estate absent cabbage"
owner_private_key = mnemonic.to_private_key(mnemonic=owner_mnemonic)
owner_wallet_address = account.address_from_private_key(owner_private_key)


algod_token = "a" *64
algod_address = "https://testnet-api.algonode.cloud"
algod_client = AlgodClient(algod_token=algod_token ,algod_address=algod_address)


params = algod_client.suggested_params()



total_supply = 1000000  # Total supply of the asset (1,000,000 units)
decimals = 0
asset_name = "Sanyam"
unit_name = "SSK"
url = "https://github.com/Sayyam-Karnavat/blockchain_mastery"



txn = transaction.AssetConfigTxn(
    sender=owner_wallet_address,
    sp=params,
    total= total_supply,
    default_frozen=False, # Whether to keep asset frozen by default
    unit_name=unit_name,
    asset_name=asset_name,
    url=url,
    manager=owner_wallet_address, # Address that can change the asset's settings
    reserve=owner_wallet_address, # Address that holds the reserve (can be set to creator)
    freeze=owner_wallet_address, # Authority to freeze and unfreeze
    clawback=owner_wallet_address, # Clawback Authority to revoke assets
    decimals=decimals
)


signed_txn = txn.sign(owner_private_key)

txid = algod_client.send_transaction(signed_txn)

print(f"Asset creation transaction ID :- {txid}")



def wait_for_completion(client:AlgodClient , txid):
    last_round = client.status().get('last-round')
    txinfo = None

    while True:
        try:
            txinfo = client.pending_transaction_info(txid)
            if txinfo.get('confirmed-round',0) > 0:
                print("Transaction Confirmed !!!")
                return txinfo
        except:
            pass
        last_round += 1
        client.status_after_block(last_round)
        time.sleep(2)

confirmed_txn = wait_for_completion(client=algod_client , txid=txid)

asset_id = confirmed_txn.get('asset-index')

print(f"Asset created :- {asset_id}")


# Get all asset ID's linked to a particular wallet address

account_info = algod_client.account_info(address=owner_wallet_address)
all_assets = account_info.get('assets' , [])


if all_assets:
    pprint.pprint(all_assets)

else:
    print("Assets found !!!!")



