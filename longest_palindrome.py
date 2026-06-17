# Day 50: Longest Palindromic Substring
# Difficulty: Medium
# Topic: Dynamic Programming
# Date: 2026-06-17

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        def expand(l, r):
            nonlocal res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1
        for i in range(len(s)):
            expand(i, i)
            expand(i, i+1)
        return res
