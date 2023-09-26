#!python3
from typing import List

def split(ls:List[int]):
    """
    Takes list of integers as parameter and returns 2 lists:
    1 containing numbers less than pivot and the other containing numbers
    greater than the pivot.
    """
    p:int = ls[0]
    less_than:List[int] = []
    greater_than:List[int] = []
    for i in range(1, len(ls)):
        if ls[i] <= p:
            less_than.append(ls[i])
        else:
            greater_than.append(ls[i])
    return less_than, greater_than

def quicksort(ls:List[int]):
    if len(ls) <= 1:
        return ls
    
    pivot:int = ls[0]
    less_than, greater_than = split(ls)
    return quicksort(less_than) + [pivot] + quicksort(greater_than)


s = [i for i in range(10, 0, -1)]
print(s)
print(quicksort(s))



    
    
