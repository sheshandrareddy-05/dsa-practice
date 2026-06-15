# Day 48: Course Schedule
# Difficulty: Medium
# Topic: Graph
# Date: 2026-06-15

from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        visited = set()
        def dfs(node):
            if node in visited: return False
            if graph[node] == []: return True
            visited.add(node)
            for nei in graph[node]:
                if not dfs(nei): return False
            visited.remove(node)
            graph[node] = []
            return True
        for c in range(numCourses):
            if not dfs(c): return False
        return True
