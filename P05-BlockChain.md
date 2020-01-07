## Problem-5: BlockChain
Blockchain implementation is simple example of a linked list. In this block chain implementation we try to keep appending the 
newer blocks to the beginning of the list. The users will have more necessity to access the newer blocks instead of accessing the older blocks.
As the need to have newer blocks more accessible, we have chosen to add the newer block to beginning of the linked list, this way 
the time complexity for inserting or accessing the newer block will be O(1).
Blockchain typically doesn't perform any deletes, hence no delete function was implemented. 

The space complexity for this implementation will be O(n), where n is the number of blocks in the blockchain. 

However, when needed to get to the oldest block, we will need to traverse to all the blocks linearly.
  
 