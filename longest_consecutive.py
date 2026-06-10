# Day 43: Longest Consecutive Sequence
# Difficulty: Medium
# Topic: HashSet
# Date: 2026-06-10

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                max_len = max(max_len, length)
        return max_len
