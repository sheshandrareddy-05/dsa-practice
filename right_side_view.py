# Day 109: Binary Tree Right Side View
# Difficulty: Medium
# Topic: BFS / DFS
# Date: 2026-08-31

from typing import List
from collections import deque

class Solution:
    def rightSideView(self, root) -> List[int]:
        if not root: return []
        res = []
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if i == len(queue): res.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return res
