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
        nums_len = len(nums)
        res = [1] * nums_len
        prefix = 1
        for i in range(nums_len):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(nums_len - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res


# @lc code=end
