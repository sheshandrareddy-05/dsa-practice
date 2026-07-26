# Day 85: Redundant Connection
# Difficulty: Medium
# Topic: Union Find
# Date: 2026-07-26

from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        rank = [1] * (len(edges) + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return False
            if rank[px] < rank[py]: px, py = py, px
            parent[py] = px
            rank[px] += rank[py]
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
