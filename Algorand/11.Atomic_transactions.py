from algosdk import transaction
from algosdk.v2client.algod import AlgodClient
from algosdk import mnemonic , account
import time




owner_mnemonic = "toss transfer sure frozen real jungle mouse inch smoke derive floor alter ten eagle narrow perfect soap weapon payment chaos amateur height estate absent cabbage"
owner_private_key = mnemonic.to_private_key(mnemonic=owner_mnemonic)
owner_wallet_address = account.address_from_private_key(owner_private_key)


print(f"Owner : \n Address:- {owner_wallet_address} \n Private key :- {owner_private_key}")


# Receiver
# reciever_private_key , receiver_wallet_address = account.generate_account()
reciever_private_key , receiver_wallet_address = "49tRpNYDZjM9aBT8CuSNZf3PWZUX80V5Jfon0n3+kLSn4Grjrhj53IswELAfLf9sZZ4NQsJmPmWvvfR/nYepUQ==","U7QGVY5ODD45ZCZQCCYB6LP7NRSZ4DKCYJTD4ZNPXX2H7HMHVFI7DERJCA"
receiver_mnemonic = mnemonic.from_private_key(reciever_private_key)
print(f"Receiver : \n Address:- {receiver_wallet_address} \n Private key :- {reciever_private_key}")

# Initialize the Algod client
algod_token = "your_algod_token"
algod_address = "https://testnet-api.algonode.cloud"
algod_client = AlgodClient(algod_token, algod_address)

# Create suggested parameters
suggested_params = algod_client.suggested_params()


asset_id = 723338809

# Create transaction A (e.g., asset transfer)
txn_a = transaction.AssetTransferTxn(
    sender=owner_wallet_address,
    receiver=receiver_wallet_address,
    amt=100,
    index=asset_id,
    sp=suggested_params
)

# Create transaction B (e.g., payment)
txn_b = transaction.PaymentTxn(
    sender=owner_wallet_address,
    receiver=receiver_wallet_address,
    amt=1000000,  # Amount in microAlgos
    sp=suggested_params
)

# Group transactions
txn_group = [txn_a, txn_b]
transaction.assign_group_id(txn_group)

# Sign the transactions
signed_txns = [txn.sign(owner_private_key) for txn in txn_group]

# Send the group transaction
txid = algod_client.send_transactions(signed_txns)

# Wait for confirmation

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


wait_for_confirmation(algod_client, txid)
print(f"Atomic transaction group confirmed with txid: {txid}")