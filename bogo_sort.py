#!python3
import random
from typing import List

def is_sorted(ls:List[int]):
    for i in range(len(ls) - 1):
        if ls[i] > ls[i+1]:
            return False
    return True

def bogo_sort(ls:List[int]):
    attempts:int = 0
    while not is_sorted(ls):
        random.shuffle(ls)
        attempts += 1
    print(attempts)
    return ls
