# Day 83: Sum of Two Integers
# Difficulty: Medium
# Topic: Bit Manipulation
# Date: 2026-07-24

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b & mask:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return a if b == 0 else a & mask
