# Day 30: Max Area of Island
# Difficulty: Medium
# Topic: BFS/DFS
# Date: 2026-05-28

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        def dfs(r, c):
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]==0: return 0
            grid[r][c] = 0
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c))
        return max_area
