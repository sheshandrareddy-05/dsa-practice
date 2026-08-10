# Day 98: Maximum Profit in Job Scheduling
# Difficulty: Hard
# Topic: DP + Binary Search
# Date: 2026-08-10

from typing import List
import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [(0, 0)]  # (end_time, max_profit)
        for s, e, p in jobs:
            i = bisect.bisect_right(dp, (s, float("inf"))) - 1
            best = dp[i][1] + p
            if best > dp[-1][1]:
                dp.append((e, best))
        return dp[-1][1]
