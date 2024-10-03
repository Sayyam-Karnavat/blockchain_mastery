import hashlib


'''
How mining works :- 




Finding a Valid Hash:

The mining process is about finding a hash that starts with a certain number of leading zeros, determined by the difficulty level.
For example, if the difficulty is 3, then the valid hash must start with three zeros (000).
The nonce (a number that starts at 0) is incremented and combined with the block's data and previous hash, creating different hash values.
The miner tries different nonce values until the resulting hash satisfies the difficulty condition.
Hash Discarding:

Every hash that doesn't meet the difficulty requirement (i.e., doesn't start with the required number of zeros) is discarded.
Only the hash that satisfies the condition (e.g., 000abc123...) is considered valid.
Adding the Block to the Chain:

Once the mining process finds a valid hash, that block is finalized.
The block (including the valid hash and the associated nonce) is added to the blockchain (self.chain), making it a part of the blockchain.

'''


import hashlib

class Block:
    def __init__(self, previous_hash, data, difficulty=2) -> None:
        self.previous_hash = previous_hash
        self.data = data
        self.nonce = 0  # The value that will be changed during mining
        self.difficulty = difficulty
        self.hash = self.mine_block()  # Mine the block to find a valid hash
    
    def convert_to_hash(self):
        return hashlib.sha256((self.previous_hash + self.data + str(self.nonce)).encode()).hexdigest()

    def mine_block(self):
        """
        Mine the block by adjusting the nonce until a valid hash is found.
        """
        computed_hash = self.convert_to_hash()
        # The valid hash must start with 'difficulty' number of leading zeros
        while not computed_hash.startswith('0' * self.difficulty):
            self.nonce += 1
            computed_hash = self.convert_to_hash()
        return computed_hash

class Blockchain:
    def __init__(self, difficulty=2) -> None:
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self):
        return Block("0", "Genesis Block", difficulty=self.difficulty)

    def add_block(self, data):
        previous_block = self.chain[-1]
        previous_block_hash = previous_block.hash
        new_block = Block(previous_hash=previous_block_hash, data=data, difficulty=self.difficulty)
        self.chain.append(new_block)

    def print_chain(self):
        for i, block in enumerate(self.chain):
            print(f"Block {i}")
            print(f"Data: {block.data}")
            print(f"Hash: {block.hash}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Nonce: {block.nonce}")
            print("-" * 64)

# Testing the code with different difficulties
blockchain = Blockchain(difficulty=3)  # Set a difficulty of 3 (hash must start with '000')

blockchain.add_block("Transaction 1")
blockchain.add_block("Transaction 2")

blockchain.print_chain()
