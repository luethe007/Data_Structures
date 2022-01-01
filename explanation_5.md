## Blockchain
A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a pointer to the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

### Time Complexity
The blockchain is implemented with a linked list which keeps track of the tail. Since we constantly update the tail of the blockchain, it is not necessary to iterate through all blocks in the chain. Appending new blocks to the blockchain works in constant time O(1).

The function __repr__ defines the object representation in string format. All the records in the blockchain will be returned as a string. This requires looping through all the records in the blockchain. Therefore, the time complexity is O(n).

### Space Complexity
The required space for the blockchain depends on the amount of blocks appended to it. Each block itself requires a constant space O(1), however the whole blockchain scales linearly with O(n) space complexity.
