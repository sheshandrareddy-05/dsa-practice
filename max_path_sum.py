# Day 111: Binary Tree Maximum Path Sum
# Difficulty: Hard
# Topic: Binary Tree DFS
# Date: 2026-09-05

class Solution:
    def maxPathSum(self, root) -> int:
        self.res = root.val
        def dfs(node):
            if not node: return 0
            left  = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            self.res = max(self.res, node.val + left + right)
            return node.val + max(left, right)
        dfs(root)
        return self.res
