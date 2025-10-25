#
# @lc app=leetcode id=1822 lang=python3
#
# [1822] Sign of the Product of an Array
#

# @lc code=start

# * Math Solution | O(n) Time | O(1) Space
# * n -> The length of nums array


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for num in nums:
            if num == 0:
                return num
            elif num < 0:
                sign = -sign

        return sign


# @lc code=end
