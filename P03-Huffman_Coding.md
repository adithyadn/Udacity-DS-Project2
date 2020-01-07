# **Problem-3: Huffman Coding**

### **Analysis:**
1. HashMap: For this implementation we have used two hash maps. One hash map was used to calculate and store the letter frequency count in the given input data. 
Second Hash Map was used to store the huffman codes for each unique letter. Usage of Hash Maps makes the usage (read/ write)
with a O(1) time complexity. 

2. Priority Queue: A priority queue was used to store the possible Nodes of the huffman tree in a order so that while we pop 
an element from the queue it return a node with least frequency. Priority Queue insert has time complexity of O(nlogn) as 
we try to maintain the queue in a sorted fashion after each new insert. while the pop of the priority queue still remains to be O(1)
time complexity. 

3. Binary Tree: Once we built the priority will all the letter nodes, we try to build a Huffman tree. 

For Huffman coding algorithm the time and space complexity for this process will be O(nlogn).   

