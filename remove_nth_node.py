# Day 34: Remove Nth Node From End
# Difficulty: Medium
# Topic: Linked List
# Date: 2026-06-01

class Solution:
    def removeNthFromEnd(self, head, n: int):
        dummy = type(head)(0)
        dummy.next = head
        fast = slow = dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
