# Day 100: Serialize and Deserialize Binary Tree
# Difficulty: Hard
# Topic: Tree + BFS
# Date: 2026-08-14

from collections import deque

class Codec:
    def serialize(self, root) -> str:
        if not root: return ""
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("N")
        return ",".join(res)

    def deserialize(self, data: str):
        if not data: return None
        vals = data.split(",")
        # Use a placeholder class — works with any TreeNode-like object
        class N:
            def __init__(self, v): self.val=v; self.left=self.right=None
        root = N(int(vals[0]))
        queue = deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if vals[i] != "N":
                node.left = N(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "N":
                node.right = N(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root
