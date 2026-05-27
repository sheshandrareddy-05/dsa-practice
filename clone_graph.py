# Day 29: Clone Graph
# Difficulty: Medium
# Topic: Graph
# Date: 2026-05-27

from collections import deque

class Solution:
    def cloneGraph(self, node):
        if not node: return None
        clones = {node: type(node)(node.val)}
        queue = deque([node])
        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = type(neighbor)(neighbor.val)
                    queue.append(neighbor)
                clones[curr].neighbors.append(clones[neighbor])
        return clones[node]
