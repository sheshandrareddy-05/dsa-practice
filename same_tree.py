# Day 105: Same Tree
# Difficulty: Easy
# Topic: Binary Tree
# Date: 2026-08-26

class Solution:
    def isSameTree(self, p, q) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
