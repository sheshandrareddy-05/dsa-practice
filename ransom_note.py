# Day 19: Ransom Note
# Difficulty: Easy
# Topic: HashMap
# Date: 2026-05-15

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = Counter(magazine)
        for c in ransomNote:
            if mag[c] <= 0: return False
            mag[c] -= 1
        return True
