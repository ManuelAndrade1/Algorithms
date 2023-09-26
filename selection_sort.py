#!python3
from typing import List

def index_of_min(ls:List[int]):
    index:int = 0
    for i in range(1, len(ls)):
        if ls[i] < ls[index]:
            index = i
    return index

def selection_sort(ls:List[int]):
    res:List[int] = []
    for i in range(len(ls)):
        index_to_move = index_of_min(ls)
        res.append(ls.pop(index_to_move))
    return res


