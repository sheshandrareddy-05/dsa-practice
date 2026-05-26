# Day 28: Binary Tree Level Order Traversal
# Difficulty: Medium
# Topic: BFS
# Date: 2026-05-26

from typing import List, Optional
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[object]) -> List[List[int]]:
        if not root: return []
        result = []
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(level)
        return result
