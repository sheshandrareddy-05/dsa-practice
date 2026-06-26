# Day 58: Subsets
# Difficulty: Medium
# Topic: Backtracking
# Date: 2026-06-26

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return
            subset.append(nums[i])   # include
            dfs(i + 1, subset)
            subset.pop()             # exclude
            dfs(i + 1, subset)
        dfs(0, [])
        return res
