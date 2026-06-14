# Day 47: Pacific Atlantic Water Flow
# Difficulty: Medium
# Topic: BFS/DFS
# Date: 2026-06-14

from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        def bfs(starts, visited):
            queue = deque(starts)
            visited.update(starts)
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and heights[nr][nc]>=heights[r][c]:
                        visited.add((nr,nc))
                        queue.append((nr,nc))
        bfs([(r,0) for r in range(rows)]+[(0,c) for c in range(cols)], pac)
        bfs([(r,cols-1) for r in range(rows)]+[(rows-1,c) for c in range(cols)], atl)
        return [[r,c] for r in range(rows) for c in range(cols) if (r,c) in pac and (r,c) in atl]
