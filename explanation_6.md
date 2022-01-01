## Union and Intersection
The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

We will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively.

### Time and Space Complexity
#### Union
The union function loops through both linked lists. I added the time complexities in the code. For bigger inputs, the code scales linearly (both time and space complexity) with the amount of items in the inputted linked lists, resulting in complexity O(n).

#### Intersection
The intersection code uses nested loops to compare the node's values of the different linked lists. Therefore, this can lead to a high computational effort O(n*m). Due to the nature of an intersection, the required space will not scale as a product of the lengths of both linked lists. The space complexity is limited to the length of the bigger linked list, resulting in space complexity O(n).
