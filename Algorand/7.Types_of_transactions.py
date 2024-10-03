import time
from algosdk import transaction

'''
### Types of Transactions on Algorand

Algorand supports several types of transactions. Here are the most common ones:

 - Payment Transactions: Used to transfer Algos between accounts.
 - Asset Transfer Transactions: Used to transfer Algorand Standard Assets (ASAs) between accounts.
 - Asset Configuration Transactions: Used to create, modify, or destroy ASAs.
 - Application Call Transactions: Used to interact with smart contracts on the Algorand blockchain.



### Structure of a Transaction 

Sender: The address initiating the transaction.
Receiver: The address that will receive the transaction (funds or assets).
Amount: The amount of Algos (or assets) being transferred.
Transaction Fee: The network fee for processing the transaction (paid in Algos).
Genesis ID: A string representing the genesis block, ensuring the transaction belongs to the right network (MainNet, TestNet, etc.).
Genesis Hash: The hash of the genesis block.
Note: An optional field to include additional data.
Transaction Parameters: Suggested network parameters such as fee, first valid round, last valid round, and so on.




'''



####################################################################################################################

                # Payment transaction #
'''

Payment transactions steps :- 

    The key steps involved:
    Set up the Algod client.
    Define sender and receiver accounts.
    Get the current transaction parameters.
    Create and sign the transaction.
    Send the transaction to the network.
    Wait for confirmation.

'''




# Small function to check if transaction is confirmed or not 

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

