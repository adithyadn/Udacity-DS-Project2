## **Problem-6: List Operations**
There two approaches for implementing union and intersection operations on a Linked Lists.

Assume size of list 1 = n and size of list 2 = m

##### **Approach-1:**

Brute Force approach. For each node in list 1, iterate over each element in list2 to perform either a union or intersection.
The time complexity of this approach is O(n*m). This is equivalent to O(n^2). However in this approach we would not need any 
additional space for performing these operations. 

We can perform slightly better on time, if we can use some additional space. 

**Approach-2:** 

Union: Make use of a set to keep track of elements which are already traversed. Iterate over the list1 and keep adding elements to 
the output list. Once list1 is completely iterated, iterate the list 2 and add elements to output list. While adding elements 
to the output_list use the set to verify if the element was already added to output. If the element was not added earlier, add the 
element to the set and to the output_list else skip the element and continue. 

Time Complexity: O(n+m); approx. O(n)

Space Complexity: O(n+m); approx. O(n+m)

Intersection: Make use of a HashMap to keep track of element which are already traversed. Additional to the key, 
we maintain the value to indicate whether the given key was traversed in list1 or list2. If the element was traversed in list2 the value for this key in the map would True. 
Similar to approach taken for performing union, we will iterate the lists1 and list2 separately and add only those elements which are in both 
list 1 and list2. 

Time Complexity: O(n+m)

Space Complexity: O(n+m) 