# Day 104: Invert Binary Tree
# Difficulty: Easy
# Topic: Binary Tree
# Date: 2026-08-25

class Solution:
    def invertTree(self, root):
        if not root: return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
