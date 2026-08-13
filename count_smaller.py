# Day 99: Count of Smaller Numbers After Self
# Difficulty: Hard
# Topic: Merge Sort / Fenwick Tree
# Date: 2026-08-13

from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        indices = list(range(len(nums)))

        def merge_sort(idx):
            if len(idx) <= 1: return idx
            mid = len(idx) // 2
            left = merge_sort(idx[:mid])
            right = merge_sort(idx[mid:])
            merged = []
            r = 0
            for l_idx in left:
                while r < len(right) and nums[right[r]] < nums[l_idx]:
                    r += 1
                result[l_idx] += r
                merged.append(l_idx)
            return merged + right

        merge_sort(indices)
        return result
