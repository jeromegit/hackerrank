#!/bin/python3
import math
import os
import random
import re
import sys

import unittest

# Vector version of all 3x3 magic squares
# Source: http://www.dr-mikes-math-games-for-kids.com/3x3-magic-square.html
all_magic_squares = [
    [2, 7, 6, 9, 5, 1, 4, 3, 8],
    [2, 9, 4, 7, 5, 3, 6, 1, 8],
    [4, 3, 8, 9, 5, 1, 2, 7, 6],
    [4, 9, 2, 3, 5, 7, 8, 1, 6],
    [6, 1, 8, 7, 5, 3, 2, 9, 4],
    [6, 7, 2, 1, 5, 9, 8, 3, 4],
    [8, 1, 6, 3, 5, 7, 4, 9, 2],
    [8, 3, 4, 1, 5, 9, 6, 7, 2],
]

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    vector = []
    [[vector.append(s[x][y]) for x in range(3)] for y in range(3)] # turn 2D matrix into vector

    minDiff = sys.maxsize
    for ms in all_magic_squares:
        diff = 0
        for i in range(9):
            diff += abs(ms[i] - vector[i])
        if diff < minDiff:
            minDiff = diff

    return minDiff

# Test cases
class FormingMagicSquareTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(formingMagicSquare([[4, 9, 2], [3, 5, 7], [8, 1, 5]]), 1)
        
    def test2(self):
        self.assertEqual(formingMagicSquare([[4, 8, 2], [4, 5, 7], [6, 1, 6]]), 4)

if __name__ == '__main__':
    unittest.main()

                                            
