# Day 21: Squares of Sorted Array
# Difficulty: Easy
# Topic: Two Pointers
# Date: 2026-05-17

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        l, r = 0, len(nums)-1
        pos = len(nums)-1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[pos] = nums[l]**2; l += 1
            else:
                res[pos] = nums[r]**2; r -= 1
            pos -= 1
        return res
