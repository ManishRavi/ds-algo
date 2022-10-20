#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start

# * Bucket Sort Solution | O(nlogk) Time | O(n) Space
# * n -> The length of words array | k -> The given input


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_counter = collections.Counter(words)
        # * Index -> Count | Value -> Array
        buckets = [[] for _ in range(len(words_counter) + 1)]
        for word, count in words_counter.items():
            buckets[count].append(word)

        res = []
        # * Start from the end of the bucket.
        for i in range(len(buckets) - 1, 0, -1):
            for word in sorted(buckets[i]):
                res.append(word)
                if len(res) == k:
                    return res


# @lc code=end
