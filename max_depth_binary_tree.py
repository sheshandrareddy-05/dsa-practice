# Day 17: Maximum Depth of Binary Tree
# Difficulty: Easy
# Topic: Binary Tree
# Date: 2026-05-12

class Solution:
    def maxDepth(self, root) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
