# Day 31: Find Minimum in Rotated Sorted Array
# Difficulty: Medium
# Topic: Binary Search
# Date: 2026-05-29

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
