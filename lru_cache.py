# Day 69: LRU Cache
# Difficulty: Medium
# Topic: Design + HashMap + DLL
# Date: 2026-07-09

class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node()  # LRU end (dummy)
        self.right = Node() # MRU end (dummy)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def insert(self, node):  # insert at MRU end
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
