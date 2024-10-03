from algosdk import mnemonic , transaction , account
from algosdk.v2client.algod import AlgodClient

algod_token = "a" * 64
algod_address = "https://testnet-api.algonode.cloud"

algod_client = AlgodClient(algod_token=algod_token , algod_address=algod_address)


# Master wallet 
master_mnemonic = "shadow wear public casino connect dolphin cat analyst vintage extend review fossil gossip apple file hurdle gain coffee foil web surround boy surprise ability lazy"
master_private_key = mnemonic.to_private_key(mnemonic=master_mnemonic)
master_wallet_address = account.address_from_private_key(master_private_key)

print("Master wallet :- " , master_wallet_address)
print("Master Private key :-" , master_private_key)


receiver_private_key , receiver_address = account.generate_account()

params = algod_client.suggested_params()

amount = 1000000  # Amount in microAlgos (1 Algo = 1,000,000 microAlgos)

txn = transaction.PaymentTxn(sender=master_wallet_address , receiver=receiver_address ,sp= params , amt= amount)


signed_txn = txn.sign(master_private_key)

txid = algod_client.send_transaction(signed_txn)

transaction.wait_for_confirmation(algod_client= algod_client , txid= txid)


print("Payment completed !!!" , txid)

