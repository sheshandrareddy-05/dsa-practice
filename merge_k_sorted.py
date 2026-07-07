# Day 67: Merge K Sorted Lists
# Difficulty: Hard
# Topic: Heap
# Date: 2026-07-07

from typing import List, Optional
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[object]]) -> Optional[object]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        dummy = type(lists[0])(0) if lists and lists[0] else None
        if not dummy: return None
        curr = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next
