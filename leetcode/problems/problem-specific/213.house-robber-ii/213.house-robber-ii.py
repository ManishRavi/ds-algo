#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start

# * Iterative Bottom-Up Solution | O(n) Time | O(1) Space
# * n -> The length of nums array


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]

        return max(self.robHelper(nums[1:]), self.robHelper(nums[:-1]))

    def robHelper(self, nums):
        rob1 = rob2 = 0
        for num in nums:
            rob1, rob2 = rob2, max(num + rob1, rob2)

        return rob2


# @lc code=end
