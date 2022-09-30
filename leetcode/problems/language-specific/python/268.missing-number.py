#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start

# * Math Solution | O(n) Time | O(1) Space
# * n -> The length of nums array


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return ((n * (n + 1)) // 2) - sum(nums)


# @lc code=end
