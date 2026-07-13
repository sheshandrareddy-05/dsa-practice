# Day 73: Target Sum
# Difficulty: Medium
# Topic: Dynamic Programming
# Date: 2026-07-13

from typing import List
from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for num in nums:
            next_dp = defaultdict(int)
            for s, count in dp.items():
                next_dp[s + num] += count
                next_dp[s - num] += count
            dp = next_dp
        return dp[target]
