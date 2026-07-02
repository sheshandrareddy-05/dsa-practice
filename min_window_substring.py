# Day 62: Minimum Window Substring
# Difficulty: Hard
# Topic: Sliding Window
# Date: 2026-07-02

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t: return ""
        need = Counter(t)
        have, want = 0, len(need)
        window = {}
        res, res_len = [-1, -1], float("inf")
        left = 0
        for right, c in enumerate(s):
            window[c] = window.get(c, 0) + 1
            if c in need and window[c] == need[c]:
                have += 1
            while have == want:
                if right - left + 1 < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""
