# Day 46: Set Matrix Zeroes
# Difficulty: Medium
# Topic: Array
# Date: 2026-06-13

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = set(), set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in rows or c in cols:
                    matrix[r][c] = 0
