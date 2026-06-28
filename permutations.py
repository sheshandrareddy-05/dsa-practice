# Day 59: Permutations
# Difficulty: Medium
# Topic: Backtracking
# Date: 2026-06-28

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(current, remaining):
            if not remaining:
                res.append(current[:])
                return
            for i in range(len(remaining)):
                current.append(remaining[i])
                dfs(current, remaining[:i] + remaining[i+1:])
                current.pop()
        dfs([], nums)
        return res
