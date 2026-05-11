# Day 16: Middle of Linked List
# Difficulty: Easy
# Topic: Linked List
# Date: 2026-05-11

class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
