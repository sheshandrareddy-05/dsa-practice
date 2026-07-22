# Day 81: Reverse Bits
# Difficulty: Easy
# Topic: Bit Manipulation
# Date: 2026-07-22

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result
