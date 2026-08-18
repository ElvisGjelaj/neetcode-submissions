import heapq
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        heap = []
        users = self.following[userId] | {userId}

        for user in users:
            if self.tweets[user]:
                index = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][index]
                heapq.heappush_max(
                    heap, (time, tweetId, user, index)
                )

        while heap and len(feed) < 10:
            time, tweetId, user, idx = heapq.heappop_max(heap)
            feed.append(tweetId)

            if idx > 0:
                idx -= 1
                time, tweetId = self.tweets[user][idx]

                heapq.heappush_max(
                    heap, (time, tweetId, user, idx)
                )

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
