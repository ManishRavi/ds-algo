#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start

# * Kadane's Algorithm Solution | O(n) Time | O(1) Space
# * n -> The length of nums array


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        cur_min = cur_max = 1
        for num in nums:
            cur_min, cur_max = min(num, num * cur_min, num * cur_max), max(
                num, num * cur_min, num * cur_max
            )
            max_product = max(max_product, cur_max)

        return max_product


# @lc code=end
