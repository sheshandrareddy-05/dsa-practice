# Day 91: Swim in Rising Water
# Difficulty: Hard
# Topic: Dijkstra / Binary Search
# Date: 2026-08-02

from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        heap = [(grid[0][0], 0, 0)]  # (max_elevation, r, c)
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        while heap:
            t, r, c = heapq.heappop(heap)
            if (r, c) in visited: continue
            visited.add((r, c))
            if r == n-1 and c == n-1: return t
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0<=nr<n and 0<=nc<n and (nr,nc) not in visited:
                    heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))
