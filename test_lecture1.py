import unittest
from lecture1 import linear_search, binary_search
from typing import List

A:List[int] = []
B:List[int] = [1]
C:List[int] = [i for i in range(1, 11)]
D:List[int] = [j for j in range (1, 101)]

class TestAlgorithms(unittest.TestCase):
    def test_linear_search(self):
        self.assertEqual(linear_search(A, 2), None)
        self.assertEqual(linear_search(B, 3), None)
        self.assertEqual(linear_search(B, 1), 0)
        self.assertEqual(linear_search(C, 4), 3)
        self.assertEqual(linear_search(C, 9), 8)
        self.assertEqual(linear_search(D, 45), 44)
    
    def test_binary_search(self):
        self.assertEqual(binary_search(A, 2), None)
        self.assertEqual(binary_search(B, 3), None)
        self.assertEqual(binary_search(B, 1), 0)
        self.assertEqual(binary_search(C, 4), 3)
        self.assertEqual(binary_search(C, 9), 8)
        self.assertEqual(binary_search(D, 45), 44)

unittest.main()