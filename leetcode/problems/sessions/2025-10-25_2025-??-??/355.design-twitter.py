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
        self._count = 0
        self._follower_followees_map = defaultdict(set)
        self._user_tweets_map = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._user_tweets_map[userId].append((self._count, tweetId))
        self._count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # * To get his own tweets in the news feed.
        self.follow(userId, userId)
        recent_tweets = []
        max_heap = []

        for followee_id in self._follower_followees_map[userId]:
            if followee_id in self._user_tweets_map:
                recent_tweet_index = len(self._user_tweets_map[followee_id]) - 1
                count, tweet_id = self._user_tweets_map[followee_id][recent_tweet_index]
                max_heap.append((-count, tweet_id, followee_id, recent_tweet_index - 1))

        heapify(max_heap)
        while max_heap and len(recent_tweets) < 10:
            _, tweet_id, followee_id, recent_tweet_index = heappop(max_heap)
            recent_tweets.append(tweet_id)
            if recent_tweet_index >= 0:
                count, tweet_id = self._user_tweets_map[followee_id][recent_tweet_index]
                heappush(
                    max_heap, (-count, tweet_id, followee_id, recent_tweet_index - 1)
                )

        return recent_tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self._follower_followees_map[followerId]:
            self._follower_followees_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self._follower_followees_map[followerId]:
            self._follower_followees_map[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end
