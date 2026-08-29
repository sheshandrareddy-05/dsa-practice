# Day 108: Kth Smallest Element in BST
# Difficulty: Medium
# Topic: Binary Search Tree
# Date: 2026-08-29

class Solution:
    def kthSmallest(self, root, k: int) -> int:
        stack = []
        curr = root
        count = 0
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            count += 1
            if count == k: return curr.val
            curr = curr.right
