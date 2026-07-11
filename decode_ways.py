# Day 71: Decode Ways
# Difficulty: Medium
# Topic: Dynamic Programming
# Date: 2026-07-11

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(s) + 1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
        return dp[len(s)]
