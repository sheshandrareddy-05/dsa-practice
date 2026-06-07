# Day 40: Rotate Image
# Difficulty: Medium
# Topic: Array
# Date: 2026-06-07

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for r in range(n):
            for c in range(r+1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        for r in range(n):
            matrix[r].reverse()
