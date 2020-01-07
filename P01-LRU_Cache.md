# **Problem-1: LRU Cache**

### **Choice of data structure:**
For implementing LRU Cache, we used two data structures:

1. HashMap: Hashmap is used to maintain the key-value pair combinations which helps the put and get operations be performed with O(1) time complexity.
We have used a basic hash function which might lead to collisions, to handle such collisions, we have chosen to store the key-value pairs as LinkedList in each bucket. 
As the size of the Cache is restricted to only 5 and when the cache overflow we remove the least recent used items, this way the use of basic hash function may not result as many collision as it would result in it's regular usage. 

2. Queue: A queue is used to maintain the order in which the cache is in "use". The oldest elements in the queue will be removed when the cache is full. This is FIFO concept of queues. 
We have used inbuilt list data structure of python and emulated the queue behavior by writing our helper code. 

### **Time And Space Complexity:**

Time Complexity: For Get and Set operations on the queue we see a average complexity of O(1). 

Space Complexity: Apart from maintaining the Hashmap for Cache, we had used a list/queue to maintain the order of usage. Hence we have additional space which resulted in space complexity O(n)
