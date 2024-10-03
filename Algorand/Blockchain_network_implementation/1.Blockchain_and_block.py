import hashlib
import sys

class Block:
    def __init__(self, previous_hash, data) -> None:
        self.previous_hash = previous_hash
        self.data = data
        self.hash = self.convert_to_hash()

    def convert_to_hash(self):
        return hashlib.sha256((self.previous_hash + self.data).encode()).hexdigest()

class Blockchain:
    def __init__(self) -> None:
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("0", "Genesis Block")

    def add_block(self, data):
        previous_block = self.chain[-1]
        previous_block_hash = previous_block.hash
        new_block = Block(previous_hash=previous_block_hash, data=data)
        self.chain.append(new_block)

    def print_chain(self):
        for i, block in enumerate(self.chain):
            print(f"Block {i}")
            print(f"Data: {block.data}")
            print(f"Hash: {block.hash}")
            print(f"Previous Hash: {block.previous_hash}")
            print("-" * 64)

if __name__ == "__main__":
    blockchain_network = Blockchain()

    while True:
        print("1 - Add block")
        print("2 - Print Chain")
        print("3 - Exit system")

        user_input = int(input("Select option: "))
        
        if user_input == 1:
            user_data = input("Enter data to be added: ")
            # Fix: add the block to the blockchain here
            blockchain_network.add_block(user_data)  # This line was missing in your code
        elif user_input == 2:
            blockchain_network.print_chain()
        elif user_input == 3:
            print("Exiting!")
            sys.exit(0)
        else:
            print("Select a valid option")
            continue
