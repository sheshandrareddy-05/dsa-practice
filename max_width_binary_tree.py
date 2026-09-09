# Day 114: Maximum Width of Binary Tree
# Difficulty: Medium
# Topic: BFS
# Date: 2026-09-09

from collections import deque

class Solution:
    def widthOfBinaryTree(self, root) -> int:
        if not root: return 0
        max_width = 0
        queue = deque([(root, 0)])  # (node, index)
        while queue:
            level_len = len(queue)
            _, first_idx = queue[0]
            for _ in range(level_len):
                node, idx = queue.popleft()
                if node.left:  queue.append((node.left,  2 * idx))
                if node.right: queue.append((node.right, 2 * idx + 1))
            max_width = max(max_width, idx - first_idx + 1)
        return max_width
