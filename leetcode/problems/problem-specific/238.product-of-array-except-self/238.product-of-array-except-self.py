#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start

# * Prefix & Suffix Products Solution | O(n) Time | O(1) Space
# * n -> The length of nums array

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)
        result = [1] * nums_length
        prefix = 1
        for i in range(nums_length):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(nums_length-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result

# @lc code=end
