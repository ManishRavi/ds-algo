#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start

# * Kadane's Algorithm Solution | O(n) Time | O(1) Space
# * n -> The length of nums array


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = min_sum = nums[0]
        cur_max_sum = cur_min_sum = total_sum = 0
        for num in nums:
            cur_max_sum = max(num, num + cur_max_sum)
            cur_min_sum = min(num, num + cur_min_sum)
            max_sum = max(max_sum, cur_max_sum)
            min_sum = min(min_sum, cur_min_sum)
            total_sum += num

        return max(max_sum, total_sum - min_sum) if max_sum >= 0 else max_sum


# @lc code=end
