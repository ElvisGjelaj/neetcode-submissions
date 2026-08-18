import heapq
class Twitter:

    def __init__(self):
        self.following = {}
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))


    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        following = self.following.get(userId, set())

        for author, tweetId in reversed(self.tweets):
            if author in following or author == userId:
                feed.append(tweetId)

            if len(feed) == 10:
                break 
        
        return feed
                
        


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)


        
