# **Problem-2: File Recursion**

### **Choice of data structure:**
For implementation of this problem we have chosen to use a stack to maintain all the files or directories which are yet to be processed. 
When we encounter a directory, we list all the files and stored them into a stack. There after we try to pop one element at a time from the stack to identify if it a file which ends with certain suffix. 
If the element in the stack is a directory a similar process of listing files and adding those values into stack is repeated until the stack is emtpy. 

### **Time And Space Complexity:**
The time complexity for this implementation is O(n) as we would need to visit every file/ directory once. To track the depth of recursion we use a stack to track the if all files/ directories are traversed. Usage of this additional space for a stack is O(n).
 