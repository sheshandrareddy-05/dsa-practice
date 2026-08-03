# Day 92: Reconstruct Itinerary
# Difficulty: Hard
# Topic: Graph / Euler Path
# Date: 2026-08-03

from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
        res = []
        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            res.append(airport)
        dfs("JFK")
        return res[::-1]
