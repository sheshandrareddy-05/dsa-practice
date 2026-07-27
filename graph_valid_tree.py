# Day 86: Graph Valid Tree
# Difficulty: Medium
# Topic: Union Find / BFS
# Date: 2026-07-27

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return False
            parent[px] = py
            return True

        return all(union(u, v) for u, v in edges)
