# Day 18: First Bad Version
# Difficulty: Easy
# Topic: Binary Search
# Date: 2026-05-13

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
