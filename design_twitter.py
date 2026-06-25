# Day 57: Design Twitter
# Difficulty: Medium
# Topic: Heap/OOP
# Date: 2026-06-25

import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list)  # userId -> [(timestamp, tweetId)]
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1  # lower = more recent for min-heap trick

    def getNewsFeed(self, userId: int) -> list:
        min_heap = []
        self.following[userId].add(userId)
        for uid in self.following[userId]:
            if uid in self.tweets:
                idx = len(self.tweets[uid]) - 1
                cnt, tid = self.tweets[uid][idx]
                heapq.heappush(min_heap, (cnt, tid, uid, idx - 1))
        res = []
        while min_heap and len(res) < 10:
            cnt, tid, uid, idx = heapq.heappop(min_heap)
            res.append(tid)
            if idx >= 0:
                cnt2, tid2 = self.tweets[uid][idx]
                heapq.heappush(min_heap, (cnt2, tid2, uid, idx - 1))
        return res

    def follow(self, f, fd): self.following[f].add(fd)
    def unfollow(self, f, fd): self.following[f].discard(fd)
