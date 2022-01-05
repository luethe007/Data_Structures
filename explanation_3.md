## Huffman Coding
Huffman coding is a lossless data compression algorithm. The algorithm assigns prefix codes to characters of a string. These prefix codes are concatenated to a bit string, representing the encoded data. This bit string requires less storage capacity without losing any information.

### Time Complexity
The Huffman coding algorithm is implemented with a dictionary, HeapQ (priority queue) and binary tree nodes.
The operations on the priority queue such as pushing and popping nodes work in O(log(n)). This needs to be done for all the characters, O(n).

In the end, the time complexity of the Huffman coding algorithm is O(nlogn).

### Space Complexity
The space complexity scales linearly. The space complexity is O(n). For example, the priority queue could double in size if the input string doubles. The Huffman tree would also increase in case of longer input strings.