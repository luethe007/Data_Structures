# %%
import os
def find_files(suffix: str, path: str) -> list:
    """
        Finds all files matching suffix recursively and returns list of paths.
        :param suffix: suffix of the files to be returned
        :param path: directory path to search through
        :return: list of file paths matching the suffix
    """
    elems = os.listdir(path) # Get list of elements
    paths = list()
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
    print(find_files(".c", "testdir")) # returns ['testdir/t1.c', 'testdir/subdir3/subsubdir1/b.c', 'testdir/subdir5/a.c', 'testdir/subdir1/a.c']


if __name__ == "__main__":
    test_find_files()
# %%
