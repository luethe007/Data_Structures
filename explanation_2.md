## File Recursion
Find all files beneath path with file name suffix.  
The function **find_files()** walks recursively through the given path and returns a list of file paths matching the suffix.

### Time Complexity
The code walks recursively through the path's folders and files. The function os.listdir() returns the elements in a given path. We look at every element (folder or file) once. For each new folder or file, it grows in constant time. Therefore, the time complexity is O(n).

### Space Complexity
The recursion creates new instances of the same function and thus requires stack space. Each new sub-directory requires another function call. If we consider the costs for each function call *m* and the recursion depth *n*, then the space complexity will be O(nm).