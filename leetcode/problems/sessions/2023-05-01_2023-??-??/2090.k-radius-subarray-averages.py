#
# @lc app=leetcode id=2090 lang=python3
#
# [2090] K Radius Subarray Averages
#

# @lc code=start

# * Prefix Sum Solution | O(n) Time | O(n) Space
# * n -> The length of nums array


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        nums_len = len(nums)
        window_size = 2 * k + 1
        res = [-1] * (nums_len)
        if nums_len < window_size:
            return res

        prefix_sum = [0] * (nums_len + 1)
        for i in range(nums_len):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        for i in range(k, nums_len - k):
            res[i] = (prefix_sum[i + k + 1] - prefix_sum[i - k]) // window_size

        return res


# @lc code=end
