#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#

# @lc code=start

# * Priority Queue (Max Heap) Solution | O(k) Time | O(n) Space
# * n -> The number of users and tweets | k -> The number of followees


class Twitter:
    def __init__(self):
        self.cnt = 0
        self.follower_followee_map = defaultdict(set)
        self.user_tweets_map = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets_map[userId].append((self.cnt, tweetId))
        self.cnt += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follow(userId, userId)
        max_heap = []
        for followeeId in self.follower_followee_map[userId]:
            if followeeId in self.user_tweets_map:
                recent_tweet_index = len(self.user_tweets_map[followeeId]) - 1
                tweet_cnt, tweet_id = self.user_tweets_map[followeeId][
                    recent_tweet_index
                ]
                max_heap.append(
                    (-tweet_cnt, tweet_id, followeeId, recent_tweet_index - 1)
                )

        heapify(max_heap)
        recent_tweets = []
        while max_heap and len(recent_tweets) < 10:
            _, tweet_id, followeeId, recent_tweet_index = heappop(max_heap)
            recent_tweets.append(tweet_id)
            if recent_tweet_index >= 0:
                tweet_cnt, tweet_id = self.user_tweets_map[followeeId][
                    recent_tweet_index
                ]
                heappush(
                    max_heap, (-tweet_cnt, tweet_id, followeeId, recent_tweet_index - 1)
                )

        return recent_tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follower_followee_map[followerId]:
            self.follower_followee_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower_followee_map[followerId]:
            self.follower_followee_map[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end
