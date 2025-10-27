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
        buckets = [[] for _ in range(len(nums) + 1)]
        nums_counter = Counter(nums)
        for num, count in nums_counter.items():
            buckets[count].append(num)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res


# @lc code=end
