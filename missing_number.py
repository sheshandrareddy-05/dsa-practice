# Day 82: Missing Number
# Difficulty: Easy
# Topic: Bit Manipulation
# Date: 2026-07-23

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)
