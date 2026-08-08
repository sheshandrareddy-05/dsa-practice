# Day 96: N Queens
# Difficulty: Hard
# Topic: Backtracking
# Date: 2026-08-08

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diag = set()  # r + c
        neg_diag = set()  # r - c
        board = [["."]*n for _ in range(n)]
        res = []
        def dfs(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in cols or r+c in pos_diag or r-c in neg_diag:
                    continue
                cols.add(c); pos_diag.add(r+c); neg_diag.add(r-c)
                board[r][c] = "Q"
                dfs(r + 1)
                cols.remove(c); pos_diag.remove(r+c); neg_diag.remove(r-c)
                board[r][c] = "."
        dfs(0)
        return res
