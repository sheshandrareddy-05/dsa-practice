# Day 84: Number of Connected Components
# Difficulty: Medium
# Topic: Union Find
# Date: 2026-07-25

from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return 0
            if rank[px] < rank[py]: px, py = py, px
            parent[py] = px
            rank[px] += rank[py]
            return 1

        return n - sum(union(u, v) for u, v in edges)
