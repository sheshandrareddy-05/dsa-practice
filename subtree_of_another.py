# Day 112: Subtree of Another Tree
# Difficulty: Easy
# Topic: Binary Tree
# Date: 2026-09-06

class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        if not root: return False
        if self.isSameTree(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p, q) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
