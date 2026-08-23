# Day 102: Path Sum
# Difficulty: Easy
# Topic: Binary Tree
# Date: 2026-08-23

class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if not root: return False
        if not root.left and not root.right:
            return root.val == targetSum
        remaining = targetSum - root.val
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)
