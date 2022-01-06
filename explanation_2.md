## File Recursion
Find all files beneath path with file name suffix.  
The function **find_files()** walks recursively through the given path and returns a list of file paths matching the suffix.

### Time Complexity
The code walks recursively through the path's folders and files. The function os.listdir() returns the elements in a given path. We look at every element (folder or file) once. For each new folder or file, it grows in constant time. Therefore, the time complexity is O(n).

### Space Complexity
The recursion creates new instances of the same function and therefore requires stack space. Each new sub-directory requires another function call. In each function call, we store the list of files matching the suffix and return this list, thus appending it to the outer data structure. The space complexity is linear, it depends on the extra space for the recursive function calls and the space needed for the lists containing the matching files. Accordingly, the space complexity is linear, O(n).