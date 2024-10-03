from algosdk.v2client.algod import AlgodClient
from algosdk import account , mnemonic , transaction


master_mnemonic = "toss transfer sure frozen real jungle mouse inch smoke derive floor alter ten eagle narrow perfect soap weapon payment chaos amateur height estate absent cabbage"

master_private_key  = mnemonic.to_private_key(master_mnemonic)
master_wallet_address = account.address_from_private_key(master_private_key)

print("Master wallet address created !!!")
receiver_private_key , receiver_wallet_address = account.generate_account()


algod_token = "a" *64
algod_address = "https://testnet-api.algonode.cloud"
algod_client = AlgodClient(algod_token=algod_token ,algod_address=algod_address)
suggested_params = algod_client.suggested_params()


payment_txn = transaction.PaymentTxn(sender= master_wallet_address , receiver= receiver_wallet_address , sp=suggested_params , amt=1000000)

signed_txn = payment_txn.sign(master_private_key)

txnid = algod_client.send_transaction(signed_txn)

transaction.wait_for_confirmation(algod_client=algod_client,txid=txnid)

print("Transaction completed :- " , txnid)


###################################################################################

 # Check amount 

# This gets all account info
account_information = algod_client.account_info(address=receiver_wallet_address)

print("Account Info :- " , account_information)


balance_in_microalgos = account_information.get("amount")

actual_balance = balance_in_microalgos / 1000000


print("Balance of receiver is :- " , actual_balance)


###############################################################################

# Get block details 

block_round = 44443073
block_info = algod_client.block_info(block_round)

print(f"Block {block_round} Information:")
print(block_info)
##################################################################################




