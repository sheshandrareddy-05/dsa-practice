# Day 44: Valid Sudoku
# Difficulty: Medium
# Topic: Array
# Date: 2026-06-11

from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".": continue
                box = (r//3, c//3)
                if val in rows[r] or val in cols[c] or val in boxes[box]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[box].add(val)
        return True
