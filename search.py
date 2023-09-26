#!python3

from typing import List

# Linear Search
def linear_search(list:List[int], target:int):
    """
    Returns the index position of the target if found, else return None.
    """
    for i in range(len(list)):
        if list[i] == target:
            return i
    return None

# Binary Search
def binary_search(list:List[int], target:int):
    """
    Requirements: list has to be sorted in ascending order.
    Returns the index position of the target if found, else returns None.
    """
    # Base case: List is empty
    if len(list) == 0: return None

    mid:int = len(list) // 2
    
    if list[mid] == target: return mid
    elif list[mid] < target:
        res:int = binary_search(list[mid+1:], target)
        if not res == None: return mid + res + 1 # 1 covers "0" position of sub-lists
        return None
    else: # midpoint is higher than the target
        res:int = binary_search(list[:mid], target)
        if not res == None: return res
        return None 

