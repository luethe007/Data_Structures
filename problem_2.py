# %%
import os
def find_files(suffix: str, path: str) -> list:
    """
        Finds all files matching suffix recursively and returns list of paths.
        :param suffix: suffix of the files to be returned
        :param path: directory path to search through
        :return: list of file paths matching the suffix
    """
    if not (isinstance(suffix, str) and isinstance(path, str)):
        raise ValueError("Please insert string parameters.")

    paths = list()
    # Check if path is directory
    if not os.path.isdir(path):
        if path.endswith(suffix): # Check if file matches suffix
            paths.append(path) # Append matched file to paths
    else:
        elems = os.listdir(path) # Get list of elements
        for elem in elems: # Iterate over all elements
            full_path = os.path.join(path, elem)
            if os.path.isdir(full_path): # Check if element is directory
                paths += find_files(suffix, full_path) # Recursive call for sub-directories
            else:
                if full_path.endswith(suffix): # Check if file matches suffix
                    paths.append(full_path) # Append matched file to paths
    return paths

# %%
def test_find_files():
    """
        Tests the functionality of the file recursion.
    """
    print(find_files(".c", "testdir")) # returns ['testdir/t1.c', 'testdir/subdir3/subsubdir1/b.c', 'testdir/subdir5/a.c', 'testdir/subdir1/a.c']
    
    path = "./solution/problem2/problem2.py"
    suffix = ".py"
    print(find_files(suffix, path)) # returns ["./solution/problem2/problem2.py"]

    print(find_files("", ""))       # returns [""]

    print(find_files(None, None))   # returns ValueError

if __name__ == "__main__":
    test_find_files()
# %%
