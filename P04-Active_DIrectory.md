## **Problem-4: Active Directory**
This is simple recursion problem. For the given user and group input, we first try to identify if the user is part of the supplied group, if yes, we return True, else we return False. 
However, if the supplied group has subgroups within, then we try to repeat the same above process for each of the subgroups until we have explored all the subgroups. 

 Lets suppose we have a total of n users and m groups, then to determine if the user is part of the group, we would have 
 time complexity of O(n+m), i.e O(n) time complexity. 
 
In terms of space complexity, we dont see any additional need of space except for the recursion call stack (O(n)).
 