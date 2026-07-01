# Day 61: Subarray Sum Equals K
# Difficulty: Medium
# Topic: Prefix Sum + HashMap
# Date: 2026-07-01

from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        seen = defaultdict(int)
        seen[0] = 1
        for num in nums:
            prefix += num
            count += seen[prefix - k]
            seen[prefix] += 1
        return count
