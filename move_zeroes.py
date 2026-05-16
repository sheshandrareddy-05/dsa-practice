# Day 20: Move Zeroes
# Difficulty: Easy
# Topic: Two Pointers
# Date: 2026-05-16

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0
        for num in nums:
            if num != 0:
                nums[pos] = num
                pos += 1
        while pos < len(nums):
            nums[pos] = 0
            pos += 1
