# Day 79: Number of 1 Bits
# Difficulty: Easy
# Topic: Bit Manipulation
# Date: 2026-07-19

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1  # remove lowest set bit
            count += 1
        return count
