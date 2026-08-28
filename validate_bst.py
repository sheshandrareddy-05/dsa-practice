# Day 107: Validate Binary Search Tree
# Difficulty: Medium
# Topic: Binary Search Tree
# Date: 2026-08-28

class Solution:
    def isValidBST(self, root) -> bool:
        def dfs(node, low, high):
            if not node: return True
            if node.val <= low or node.val >= high: return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        return dfs(root, float("-inf"), float("inf"))
