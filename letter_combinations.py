# Day 60: Letter Combinations of Phone Number
# Difficulty: Medium
# Topic: Backtracking
# Date: 2026-06-29

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        phone = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = []
        def dfs(i, current):
            if i == len(digits):
                res.append(current)
                return
            for c in phone[digits[i]]:
                dfs(i + 1, current + c)
        dfs(0, "")
        return res
