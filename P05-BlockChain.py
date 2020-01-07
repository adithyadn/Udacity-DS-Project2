
import hashlib
import time

class Block:

    def __init__(self, timestamp, data, previous_hash, previous):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.previous = previous

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = str(self.data) + str(self.timestamp) + str(self.previous_hash)

        sha.update(hash_str.encode('utf-8'))

        return sha.hexdigest()

class BlockChain:

    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head is None:
            self.head = Block(time.time(), data, None, None)
        else:
            self.head = Block(time.time(), data, self.head.hash, self.head)

    def print_blocks(self):
        current = self.head
        while current:
            print("data :: " + str(current.data) + "; previous_hash :: " + str(current.previous_hash))
            current = current.previous

block_chain = BlockChain()
block_chain.add("First Block")
block_chain.add("Second Block")
block_chain.add("Third Block")

assert block_chain.head.data == "Third Block"
