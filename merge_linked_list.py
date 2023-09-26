#!python3

from linked_list import LinkedList, Node
from typing import List

def split(ls:LinkedList):
    """
    Divide unsorted LinkedList into sublists
    """
    left_half:LinkedList = None
    right_half:LinkedList = None

    if ls == None or ls.head == None:
        left_half:LinkedList = ls
        return left_half, right_half
    else:
        size:int = ls.get_size()
        mid:int = size // 2
        mid_node = ls.node_at_index(mid - 1)

        left_half = ls # Left half assigned to ls
        right_half = LinkedList() # Create new list
        right_half.head = mid_node.next # New list starts from mid node onwards
        mid_node.next = None # Mid node stayed on left half now points to none (severing the connection)

    return left_half, right_half

def merge(left:LinkedList, right:LinkedList):
    """
    Merges two linked lists
    """
    res:LinkedList = LinkedList()

    # Add a fake head that is discarded later
    res.add(0)

    curr:Node = res.head
    left_head:Node = left.head
    right_head:Node = right.head

    # Iterate over left and right until we reach teh tail node
    while left_head or right_head:
        # If the head node of left is None, we're past the tail
        # Add the node from right to merged linked list
        if left_head is None:
            curr.next = right_head
            right_head = right_head.next
        # If the head node of right is None, we're past the tail
        # Add the tail node from left to merged linked list
        elif right_head is None:
            curr.next = left_head
            left_head = left_head.next

        else:
            # Obtain node data to perform comparison operations
            l_data:int = left_head.data
            r_data:int = right_head.data
            if l_data < r_data:
                curr.next = left_head
                left_head = left_head.next
            else:
                curr.next = right_head
                right_head = right_head.next
        curr = curr.next
    head = res.head.next
    res.head = head
    return res
    
def merge_sort(ls:LinkedList):
    if ls.get_size() == 1:
        return ls
    elif ls.head is None:
        return ls
    
    left_half, right_half = split(ls)
    left:LinkedList = merge_sort(left_half)
    right:LinkedList = merge_sort(right_half)

    return merge(left, right)