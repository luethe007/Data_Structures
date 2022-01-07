# %%
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string[:-3]

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

# %%
def union(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    """
        Unions two linked lists and returns a new linked list.
    """
    list_1 = []
    list_2 = []

    # Loop through first linked list in O(n)
    node_1 = llist_1.head
    while node_1:
        list_1.append(node_1.value)
        node_1 = node_1.next
    
    # Loop through second linked list in O(m)
    node_2 = llist_2.head
    while node_2:
        list_2.append(node_2.value)
        node_2 = node_2.next

    # Remove duplicates in O(n+m)
    union_list = list(set(list_1 + list_2))

    # Create new linked list and fill with data, O(p)
    union_llist = LinkedList()
    for item in union_list:
        union_llist.append(item)
    
    return union_llist

# %%
def intersection(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    """
        Keeps intersection of two linked lists and returns a new linked list.
    """
    # Loop through both linked lists O(n*m)
    intersection_list = []
    node_1 = llist_1.head
    while node_1:
        node_2 = llist_2.head
        while node_2:
            if node_1.value == node_2.value:
                intersection_list.append(node_1.value)
                break
            node_2 = node_2.next
        node_1 = node_1.next

    # Create new linked lista and fill with data, O(p)
    intersection_llist = LinkedList()
    for item in intersection_list:
        intersection_llist.append(item)
    
    return intersection_llist

# %%
def test_func():
    """
        Tests the functionality of the union and intersection functions.
    """
    # Test case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35]
    element_2 = [6,32,4,9,3]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("Test Case 1")
    print(union(linked_list_1,linked_list_2)) # returns 32 -> 2 -> 35 -> 3 -> 4 -> 6 -> 9 
    print(intersection(linked_list_1,linked_list_2)) # returns 3 -> 4

    # Test case 2
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3,2,8,5,66]
    element_2 = [1,7,8,66]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print("Test Case 2")
    print(union(linked_list_3,linked_list_4)) # returns 1 -> 66 -> 2 -> 3 -> 5 -> 7 -> 8
    print(intersection(linked_list_3,linked_list_4)) # returns 8 -> 66

    # Test case 3
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = []
    element_2 = [1,7,8,66]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print("Test Case 3")
    print(union(linked_list_3,linked_list_4)) # returns 8 -> 1 -> 66 -> 7
    print(intersection(linked_list_3,linked_list_4)) # returns empty linked list

    # Test case 4
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = []
    element_2 = []

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print("Test Case 4")
    print(union(linked_list_3,linked_list_4)) # returns empty linked list
    print(intersection(linked_list_3,linked_list_4)) # returns empty linked list

if __name__ == "__main__":
    test_func()

# %%
