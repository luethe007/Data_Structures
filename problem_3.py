# %%
import sys
import heapq as hq

class Node:
    """
        Huffman Tree Node definition containing the character, frequency and children.
    """
    def __init__(self, char: str, freq: int) -> None:
        self.char = char
        self.freq = freq
        self.left_child = None
        self.right_child = None
    
    # Override the comparison operator
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encoding(data: str) -> tuple:
    """
        Encodes the data with Huffman Coding Algorithm.
    """

    if not isinstance(data, str):
        raise ValueError("Input is not a string.")
    
    if not data:
        raise ValueError("Empty strings cannot be encoded.")

    # Count char frequency in data, O(n)
    char_freq = {}
    for char in data:
        if char in char_freq:
            char_freq[char] += 1
        else: 
            char_freq[char] = 1
    
    # Check if data contains only one character
    if len(char_freq) == 1:
        char = list(char_freq.keys())[0]
        return "0", Node(char, char_freq[char])

    # Iterate over char_freq dict, O(n)
    heap = []
    for char, freq in char_freq.items():
        hq.heappush(heap, (freq, Node(char, freq))) # O(log(n))

    # Generate Huffman tree
    while len(heap) > 1:
        left_node = hq.heappop(heap)[1] # O(log(n))
        right_node = hq.heappop(heap)[1] # O(log(n))
        new_node = Node(char=None, freq=left_node.freq + right_node.freq)
        new_node.left_child = left_node 
        new_node.right_child = right_node
        hq.heappush(heap, (new_node.freq, new_node)) # O(log(n))

    # Depth-First-Search function to traverse the tree, O(n)
    codes = {}
    def depth_first_search(node, code):
        if not node:
            return None
        if node.char:
            codes[node.char] = code
        depth_first_search(node.left_child, code + '0')
        depth_first_search(node.right_child, code + '1')
        
    # Get root node and traverse the tree
    root_node = heap[0][1]
    depth_first_search(root_node, "")

    # Encode data by replacing chars with codes, O(n)
    encoded_data = data
    for char, code in codes.items():
        encoded_data = encoded_data.replace(char, code)

    return encoded_data, root_node


# %%
def huffman_decoding(encoded_data: str, root: Node) -> str:
    """
        Decodes Huffman encoded data. 
    """
    # Check for edge case with only one character
    if root.char:
        return root.char * root.freq

    # Iterate over bit string to decode data, O(n)
    decoded_data = ""
    node = root
    for bit in encoded_data:
        if bit == "0":
            node = node.left_child
        else:
            node = node.right_child
        if node.char:
            decoded_data += node.char
            node = root
    return decoded_data


# %%
def test_huffman_coding(a_great_sentence = "The bird is the word"):
    """
        Tests functionality of Huffman algorithm.
    """

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, root_node = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, root_node)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

if __name__ == "__main__":
        test_huffman_coding()
        test_huffman_coding("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV")
        test_huffman_coding("a")
        test_huffman_coding(None) # Returns ValueError: Input is not a string.
        test_huffman_coding("") # Returns ValueError: Empty strings cannot be encoded.
    
# %%
