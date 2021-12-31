## Active Directory
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.

### Time Complexity
The implementation uses a defaultdict and a double-ended queue (deque) from the Python collections library. The defaultdict is used to prevent revisiting groups multiple times. The double-ended queue provides optimizations for appending and popping from two different ends of the queue.  

I used a BFS approach as I assume that most users will be stored in higher-level groups.  

The amount of iterations required to find the user in the group (and sub-groups) depends on the amount of groups and users within these groups. I indicated the time complexity precisely in the code section. Due to the fact, that we might need to iterate over all groups and users, the time complexity is O(n).  


### Space Complexity
The same argumentation as for the time complexity holds true for the space complexity. The required space allocation varies with the provided input and grows linearly O(n).
