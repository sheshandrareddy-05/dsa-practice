# Day 115: Path Sum II
# Difficulty: Medium
# Topic: Backtracking
# Date: 2026-09-10

from typing import List

class Solution:
    def pathSum(self, root, targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, remaining, path):
            if not node: return
            path.append(node.val)
            if not node.left and not node.right and remaining == node.val:
                res.append(path[:])
            else:
                dfs(node.left,  remaining - node.val, path)
                dfs(node.right, remaining - node.val, path)
            path.pop()
        dfs(root, targetSum, [])
        return res
