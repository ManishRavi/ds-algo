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
        nums_length = len(nums)
        nums_counter = collections.Counter(nums)
        # * Index -> Count | Value -> Array
        bucket_list = [[] for _ in range(nums_length+1)]
        for num, num_count in nums_counter.items():
            bucket_list[num_count].append(num)

        result = []
        # * Start from the end of the bucket
        for i in range(len(bucket_list)-1, 0, -1):
            for num in bucket_list[i]:
                result.append(num)
                if len(result) == k:
                    return result

# @lc code=end
