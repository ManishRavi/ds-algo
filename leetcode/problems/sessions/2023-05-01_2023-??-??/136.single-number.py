#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start

# * Bit Manipulation Solution | O(n) Time | O(1) Space
# * n -> The length of nums array


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num

        return res


# @lc code=end
