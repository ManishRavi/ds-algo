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
        # * Stores a key-value pair where the key is a followerId and value is a followeeId.
        # * followerId -> followeeId
        self.follow_mappings = collections.defaultdict(set)
        # * Stores a key-value pair where the key is a userId and value is an array of count and tweetId.
        # * userId -> [(count, tweetId)]
        self.tweet_mappings = collections.defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_mappings[userId].append((self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # * To get his own tweets in the news feed.
        self.follow(userId, userId)
        recent_tweets = []
        max_heap = []

        # * Push the last/recent tweet of all the followees into the heap.
        for followee_id in self.follow_mappings[userId]:
            if followee_id in self.tweet_mappings:
                recent_tweet_index = len(self.tweet_mappings[followee_id]) - 1
                count, tweet_id = self.tweet_mappings[followee_id][recent_tweet_index]
                heapq.heappush(
                    max_heap,
                    (-count, tweet_id, followee_id, recent_tweet_index - 1)
                )

        while max_heap and len(recent_tweets) < 10:
            count, tweet_id, followee_id, recent_tweet_index = heapq.heappop(
                max_heap
            )
            recent_tweets.append(tweet_id)
            # * If we still have tweets available for the same followee then push it into the heap.
            if recent_tweet_index >= 0:
                count, tweet_id = self.tweet_mappings[followee_id][recent_tweet_index]
                heapq.heappush(
                    max_heap,
                    (-count, tweet_id, followee_id, recent_tweet_index - 1)
                )

        return recent_tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follow_mappings[followerId]:
            self.follow_mappings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_mappings[followerId]:
            self.follow_mappings[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end
