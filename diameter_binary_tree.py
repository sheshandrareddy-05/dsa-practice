# Day 15: Diameter of Binary Tree
# Difficulty: Easy
# Topic: Binary Tree
# Date: 2026-05-10

class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.res = 0
        def depth(node):
            if not node: return 0
            l = depth(node.left)
            r = depth(node.right)
            self.res = max(self.res, l + r)
            return max(l, r) + 1
        depth(root)
        return self.res
