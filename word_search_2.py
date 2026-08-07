# Day 95: Word Search II
# Difficulty: Hard
# Topic: Trie + Backtracking
# Date: 2026-08-07

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            curr = root
            for c in w:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = w
        rows, cols = len(board), len(board[0])
        res = []
        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children: return
            next_node = node.children[ch]
            if next_node.word:
                res.append(next_node.word)
                next_node.word = None  # avoid duplicates
            board[r][c] = "#"
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and board[nr][nc] != "#":
                    dfs(nr, nc, next_node)
            board[r][c] = ch
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        return res
