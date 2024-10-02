from algosdk import account , mnemonic

private_key , wallet_address = account.generate_account()

mnemonic_phrase = mnemonic.from_private_key(private_key)

# Print the account details
print("Account Address: ", wallet_address)
print("Mnemonic Phrase: ", mnemonic_phrase)