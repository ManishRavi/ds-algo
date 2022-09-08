#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start

# * Bucket Sort Solution | O(n) Time | O(n) Space
# * n -> The length of nums array


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_len = len(nums)
        nums_counter = collections.Counter(nums)
        # * Index -> Count | Value -> Array
        buckets = [[] for _ in range(nums_len + 1)]
        for num, count in nums_counter.items():
            buckets[count].append(num)

        res = []
        # * Start from the end of the bucket.
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res


# @lc code=end
