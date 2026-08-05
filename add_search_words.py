# Day 94: Design Add and Search Words
# Difficulty: Medium
# Topic: Trie + DFS
# Date: 2026-08-05

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(j, node):
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    return any(dfs(i+1, child) for child in node.children.values())
                if c not in node.children:
                    return False
                node = node.children[c]
            return node.end
        return dfs(0, self.root)
