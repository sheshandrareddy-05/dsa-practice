# Day 90: Cheapest Flights K Stops
# Difficulty: Medium
# Topic: Bellman-Ford / Graph
# Date: 2026-08-01

from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        for _ in range(k + 1):  # k stops = k+1 edges
            tmp = prices.copy()
            for u, v, w in flights:
                if prices[u] != float("inf") and prices[u] + w < tmp[v]:
                    tmp[v] = prices[u] + w
            prices = tmp
        return prices[dst] if prices[dst] != float("inf") else -1
