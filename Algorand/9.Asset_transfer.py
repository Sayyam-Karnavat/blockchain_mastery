####################################################################################################################

                    # Asset Transfer Transaction # 

'''
Steps :- 

1. Create or opt-in to the ASA (if needed): Before transferring an asset, both the sender and the receiver must have opted into the asset.
    
    Note :- Opting in simply means that they have added the ASA to their accounts.
            Opting in is required for the receiver to hold the asset. 



2. Asset Transfer: Once both parties have opted in, the sender can transfer the asset to the receiver.

3. Confirm the Transaction: Wait for the transaction to be confirmed by the network.



Note :- OPT - IN transaction must be signed by receiver to make it opt-in and not the owner.

'''

from algosdk import transaction , account , mnemonic
from algosdk.v2client.algod import AlgodClient
import time

# Owner
owner_mnemonic = "toss transfer sure frozen real jungle mouse inch smoke derive floor alter ten eagle narrow perfect soap weapon payment chaos amateur height estate absent cabbage"
owner_private_key = mnemonic.to_private_key(mnemonic=owner_mnemonic)
owner_wallet_address = account.address_from_private_key(owner_private_key)


print(f"Owner : \n Address:- {owner_wallet_address} \n Private key :- {owner_private_key}")


# Receiver
# reciever_private_key , receiver_wallet_address = account.generate_account()
reciever_private_key , receiver_wallet_address = "49tRpNYDZjM9aBT8CuSNZf3PWZUX80V5Jfon0n3+kLSn4Grjrhj53IswELAfLf9sZZ4NQsJmPmWvvfR/nYepUQ==","U7QGVY5ODD45ZCZQCCYB6LP7NRSZ4DKCYJTD4ZNPXX2H7HMHVFI7DERJCA"
receiver_mnemonic = mnemonic.from_private_key(reciever_private_key)
print(f"Receiver : \n Address:- {receiver_wallet_address} \n Private key :- {reciever_private_key}")



algod_token = "a" *64
algod_address = "https://testnet-api.algonode.cloud"
algod_client = AlgodClient(algod_token=algod_token ,algod_address=algod_address)


# Since receiver is compulsory to opt in to asset below is the code to opt-in

asset_id = 723338809
suggested_params = algod_client.suggested_params()

opt_in_transaction = transaction.AssetTransferTxn(
    sender=receiver_wallet_address,
    receiver= receiver_wallet_address,
    sp=suggested_params,
    amt= 0, # Optin with 0 units of the asset
    index=asset_id,
    )


opt_in_signed_txn = opt_in_transaction.sign(reciever_private_key)

optin_txid = algod_client.send_transaction(txn=opt_in_signed_txn)

def wait_for_confirmation(client, txid):
    """
    Utility function to wait until the transaction is confirmed
    """
    while True:
        try:
            pending_txn = client.pending_transaction_info(txid)
            if pending_txn.get("confirmed-round", 0) > 0:
                print(f"Transaction confirmed in round {pending_txn['confirmed-round']}")
                return pending_txn
        except Exception:
            pass
        time.sleep(2)

# Create an Opt-In to ASA(Algorand standard asset)
wait_for_confirmation(client=algod_client , txid=optin_txid)
print("Opt-In is done !!!")



# Define the amount of the asset to transfer (e.g., 10 units)
asset_amount = 10

# Create the asset transfer transaction
asset_txn = transaction.AssetTransferTxn(
    sender=owner_wallet_address,
    sp=suggested_params,
    receiver=receiver_wallet_address,
    amt=asset_amount,
    index=asset_id
)

signed_asset_txn = asset_txn.sign(owner_private_key)

asset_txid = algod_client.send_transaction(txn=signed_asset_txn)

wait_for_confirmation(algod_client, asset_txid)
print(f"Asset transfer confirmed with txid: {asset_txid}")




