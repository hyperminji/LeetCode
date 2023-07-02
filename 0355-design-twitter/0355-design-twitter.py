from heapq import heapify, heappop, heappush

class Twitter:

    def __init__(self):
        self.user_tweet = {}
        self.user_followed = {}
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweet[userId] = self.user_tweet.get(userId, [])
        heapq.heappush(self.user_tweet[userId], [self.time, tweetId])
        self.time -= 1      
        

    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweet = []
        if userId in self.user_followed:
            for followedId in self.user_followed[userId]:
                print(userId, followedId)
                if followedId in self.user_tweet:
                    for tweet in self.user_tweet[followedId]:
                        heapq.heappush(all_tweet, tweet)
        if userId in self.user_tweet:
            for tweet in self.user_tweet[userId]:
                heapq.heappush(all_tweet, tweet)
        result = []
        
        
        while all_tweet and len(result) < 10:
            result.append(heapq.heappop(all_tweet)[1])
        return result
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_followed[followerId] = self.user_followed.get(followerId, [])
        if followeeId in self.user_followed[followerId]:
            return
        self.user_followed[followerId].append(followeeId)
        print(self.user_followed)
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user_followed:
            self.user_followed[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)