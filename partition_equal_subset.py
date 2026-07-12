# Day 72: Partition Equal Subset Sum
# Difficulty: Medium
# Topic: Dynamic Programming
# Date: 2026-07-12

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False
        target = total // 2
        dp = {0}
        for num in nums:
            dp = {s + num for s in dp} | dp
            if target in dp: return True
        return False
