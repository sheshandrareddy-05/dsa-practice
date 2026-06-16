# Day 49: House Robber II
# Difficulty: Medium
# Topic: Dynamic Programming
# Date: 2026-06-16

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def rob_linear(houses):
            prev2, prev1 = 0, 0
            for num in houses:
                curr = max(prev1, prev2 + num)
                prev2, prev1 = prev1, curr
            return prev1
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
