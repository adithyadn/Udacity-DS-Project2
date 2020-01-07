import sys
class Node:
    def __init__(self, letter, frequency):
        self.letter = letter
        self.frequency = frequency
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.frequency < other.frequency
    def __str__(self):
        return "Node("+self.letter+","+self.frequency+")"

class PriorityQueue:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)
        self.data = sorted(self.data)

    def pop(self):
        return self.data.pop(0)

    def __len__(self):
        return len(self.data)

class HuffmanTree:
    def __init__(self, letter, frequency):
        self.root = Node(letter, frequency)

    def min_heapify(self, node1, node2):
        total = node1.frequency + node2.frequency
        new_node = Node("", total)

        if node1.frequency < node2.frequency:
            new_node.left = node1
            new_node.right = node2
        else:
            new_node.left = node2
            new_node.right = node1

        self.root = new_node

def generate_code_map(node, prefix, code_map):
    if node is None:
        return
    #print(node.letter + "::" + str(node.frequency) + "::" + prefix)
    if node.left is None and node.right is None:
        code_map[node.letter] = prefix
    generate_code_map(node.left, prefix+"0", code_map)
    generate_code_map(node.right, prefix+"1", code_map)

def get_letter_frequency(data):
    frequency_map = {}
    for letter in data:
        if letter not in frequency_map:
            frequency_map[letter] = 1
        else:
            frequency_map[letter] += 1
    return frequency_map

def build_priority_queue(frequency_map):
    queue = PriorityQueue()
    for key in frequency_map:
        queue.push(Node(key, frequency_map[key]))
    return queue

def huffman_encoding(data):
    frequency_map = get_letter_frequency(data)
    priority_queue = build_priority_queue(frequency_map)
    tree = HuffmanTree("", 0)

    while len(priority_queue) > 1:
        node1 = priority_queue.pop()
        node2 = priority_queue.pop()
        tree.min_heapify(node1, node2)
        priority_queue.push(tree.root)

    code_map = {}
    generate_code_map(tree.root, "", code_map)
    print(code_map)

    encoded_str = ""

    for char in data:
        encoded_str += code_map[char]

    return encoded_str, tree
    pass

def huffman_decoding(data,tree):
    current = tree.root
    decoded_str = ""
    for turn in data:
        if turn == "0":
            current = current.left
        else:
            current = current.right
        if current.left is None and current.right is None:
            decoded_str += current.letter
            current = tree.root
    return decoded_str
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))