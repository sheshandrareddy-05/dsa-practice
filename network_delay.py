# Day 89: Network Delay Time
# Difficulty: Medium
# Topic: Dijkstra / Graph
# Date: 2026-07-31

from typing import List
import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        dist = {}
        heap = [(0, k)]  # (cost, node)
        while heap:
            cost, u = heapq.heappop(heap)
            if u in dist: continue
            dist[u] = cost
            for v, w in graph[u]:
                if v not in dist:
                    heapq.heappush(heap, (cost + w, v))
        return max(dist.values()) if len(dist) == n else -1
