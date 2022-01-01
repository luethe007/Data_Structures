# %%
import hashlib
from datetime import datetime

class Block():
    """
        Record in the blockchain. Each contains the timestamp, data, a pointer to the previous
        block (previous_hash) and it's own hash.
    """
    def __init__(self, timestamp: str, data: str, previous_block):
      self.timestamp = timestamp
      self.data = data
      self.previous_block = previous_block
      self.hash = self.calc_hash()

    def calc_hash(self):
        """
            Calculates the hash code for a new block.
        """
        sha = hashlib.sha256()
        hash_str = str(self.__dict__)
        sha.update(hash_str.encode())

        return sha.hexdigest()

class Blockchain:
    """
        Linked List implementation of a sequential chain of records.
    """
    def __init__(self):
        self.tail = None
        self.num_elements = 0
        
    def append(self, data: str):
        """
            Appends a new block to the chain.
        """
        utc_time = str(datetime.utcnow())

        if self.tail is None:
            self.tail = Block(utc_time, data, None)
        else:
            self.tail = Block(utc_time, data, self.tail)
        self.num_elements += 1
                
    def size(self):
        """
            Returns size of the blockchain.
        """
        return self.num_elements
    
    def is_empty(self):
        """
            Returns True if blockchain is empty, False otherwise.
        """
        return self.num_elements == 0

    def __repr__(self):
        """
            Defines the object representation in string format.
        """
        block = self.tail
        blocks = []
        while block:
            blocks.append(block.data + " (" + block.timestamp + ") ")
            block = block.previous_block
        blocks.reverse()
        return " <- ".join(blocks)

# %%
def test_block_chain():
    """
        Tests blockchain functionality.
    """
    chain = Blockchain()
    print(chain.is_empty())         # Returns True
    print(chain.size())             # Returns 0

    chain.append("Transaction 1")
    print(chain.tail.hash)          # Returns hexdecimal hash code
    chain.append("Transaction 2")
    print(chain.tail.hash)          # Returns hexdecimal hash code
    
    print(chain.is_empty())         # Returns False
    print(chain.size())             # Returns 2

    chain.append("Bank Account withdraws Bitcoin")
    chain.append("Transfer of btc between wallets")

    print(chain)                    # Prints the records in the blockchain
    print(chain.size())             # Returns 4


if __name__ == "__main__":
    test_block_chain()


# %%