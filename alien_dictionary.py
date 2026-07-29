# Day 88: Alien Dictionary
# Difficulty: Hard
# Topic: Topological Sort
# Date: 2026-07-29

from typing import List
from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visited = {}  # False=visited, True=in_cycle
        res = []
        def dfs(c):
            if c in visited: return visited[c]
            visited[c] = True
            for nei in adj[c]:
                if dfs(nei): return True
            visited[c] = False
            res.append(c)
        for c in adj:
            if dfs(c): return ""
        res.reverse()
        return "".join(res)
