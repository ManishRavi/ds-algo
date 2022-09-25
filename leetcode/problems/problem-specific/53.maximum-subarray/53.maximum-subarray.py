#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start

# * Kadane's Algorithm Solution | O(n) Time | O(1) Space
# * n -> The length of nums array


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0
        for num in nums:
            # * Start the subarray from the current num (num) or extend the
            # * subarray using the current num (num + cur_sum).
            cur_sum = max(num, num + cur_sum)
            max_sum = max(max_sum, cur_sum)

        return max_sum


# @lc code=end
