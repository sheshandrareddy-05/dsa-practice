# Day 53: Car Fleet
# Difficulty: Medium
# Topic: Monotonic Stack
# Date: 2026-06-21

from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, spd in pairs:
            time = (target - pos) / spd
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()  # caught up, same fleet
        return len(stack)
