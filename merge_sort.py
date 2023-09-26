#!python3
from typing import List

def split(ls:List[int]):
    """
    Divides the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    """
    mid:int = len(ls) // 2
    return ls[:mid], ls[mid:]

def merge(left:List[int], right:List[int]):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list
    """
    res:List[int] = []
    i:int = 0
    j:int = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left): 
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res

def merge_sort(ls:List[int]):
    """
    Sorts a list in ascending order
    Returns a new sorted list
    """
    # Base case
    if len(ls) <= 1:
        return ls
    left_half, right_half = split(ls)
    left = merge_sort(left_half)
    right = merge_sort(right_half) 
    return merge(left, right)