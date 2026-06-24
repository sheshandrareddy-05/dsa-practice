# Day 56: Task Scheduler
# Difficulty: Medium
# Topic: Heap/Greedy
# Date: 2026-06-24

from typing import List
from collections import Counter
import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-c for c in count.values()]
        heapq.heapify(max_heap)
        time = 0
        queue = deque()  # (count, available_at)
        while max_heap or queue:
            time += 1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt: queue.append((cnt, time + n))
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
        return time
