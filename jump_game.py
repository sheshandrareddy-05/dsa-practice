# Day 39: Jump Game
# Difficulty: Medium
# Topic: Greedy
# Date: 2026-06-06

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, jump in enumerate(nums):
            if i > max_reach: return False
            max_reach = max(max_reach, i + jump)
        return True
