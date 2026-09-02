# Day 110: Construct Binary Tree from Preorder and Inorder
# Difficulty: Medium
# Topic: Binary Tree
# Date: 2026-09-02

from typing import List

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]):
        if not preorder: return None
        root_val = preorder[0]
        mid = inorder.index(root_val)
        # Use a class trick — works on LeetCode where TreeNode is defined
        class N:
            def __init__(self, v): self.val=v; self.left=self.right=None
        root = N(root_val)
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
