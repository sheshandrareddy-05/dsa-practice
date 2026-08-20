# Day 101: Palindrome Linked List
# Difficulty: Easy
# Topic: Linked List + Two Pointers
# Date: 2026-08-20

class Solution:
    def isPalindrome(self, head) -> bool:
        # Step 1: find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Step 2: reverse second half
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # Step 3: compare
        left, right = head, prev
        while right:
            if left.val != right.val: return False
            left = left.next
            right = right.next
        return True
