# %%
from collections import defaultdict, deque

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

# %%
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    # Create default dict to keep track of visited groups
    visited = defaultdict(lambda:False)

    # Create a queue for BFS
    queue = deque()

    # Enqueue the source group
    queue.append(group) # Requires O(1) time

    while queue:
        # Dequeue a group
        current_group = queue.popleft() # Requires O(1) time
        if user in current_group.users: # Requires O(n) time
            return True

        # Mark current group as visited
        visited[current_group] = True # Requires O(1) time
        
        # Get adjacent groups. If not visited, then enqueue it.
        for group in group.groups:
            if visited[group] == False: # Requires O(1) time
                queue.append(group) # Requires O(1) time
    return False

def test_func():
    """
        Tests functionality of the BFS search.
    """
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")
    shared_group = Group("sharedgroup")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    child.add_group(shared_group)
    parent.add_group(shared_group)
    parent.add_group(child)
 
    print(is_user_in_group("sub_child_user", parent)) # returns True
    print(is_user_in_group("non_existent_user", parent)) # returns False
    print(is_user_in_group("", parent)) # returns False
    print(is_user_in_group(None, parent)) # returns False

if __name__ == "__main__":
    test_func()


# %%
