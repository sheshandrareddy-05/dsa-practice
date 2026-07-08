# Day 68: Reverse Nodes in K-Group
# Difficulty: Hard
# Topic: Linked List
# Date: 2026-07-08

class Solution:
    def reverseKGroup(self, head, k: int):
        dummy = type(head)(0)
        dummy.next = head
        group_prev = dummy
        while True:
            kth = self.get_kth(group_prev, k)
            if not kth: break
            group_next = kth.next
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
        return dummy.next

    def get_kth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
