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
        self.count = 0
        # * Stores a key-value pair where the key is a followerId and value is a set of followeeIds.
        # * Key -> followerId | Value -> {followeeId}
        self.follower_followees_set_map = collections.defaultdict(set)
        # * Stores a key-value pair where the key is a userId and value is an array of count and tweetId.
        # * Key -> userId | Value -> [(count, tweetId)]
        self.user_tweets_map = collections.defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets_map[userId].append((self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # * To get his own tweets in the news feed.
        self.follow(userId, userId)
        recent_tweets = []
        max_heap = []

        # * Add the last/recent tweet of all the followees into the max_heap list.
        for followee_id in self.follower_followees_set_map[userId]:
            if followee_id in self.user_tweets_map:
                recent_tweet_index = len(self.user_tweets_map[followee_id]) - 1
                count, tweet_id = self.user_tweets_map[followee_id][recent_tweet_index]
                max_heap.append((-count, tweet_id, followee_id, recent_tweet_index - 1))

        heapq.heapify(max_heap)
        # * Build the news feed.
        while max_heap and len(recent_tweets) < 10:
            _, tweet_id, followee_id, recent_tweet_index = heapq.heappop(max_heap)
            recent_tweets.append(tweet_id)
            # * If we still have tweets available for the same followee then push it into the heap.
            if recent_tweet_index >= 0:
                count, tweet_id = self.user_tweets_map[followee_id][recent_tweet_index]
                heapq.heappush(
                    max_heap, (-count, tweet_id, followee_id, recent_tweet_index - 1)
                )

        return recent_tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follower_followees_set_map[followerId]:
            self.follower_followees_set_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower_followees_set_map[followerId]:
            self.follower_followees_set_map[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end
