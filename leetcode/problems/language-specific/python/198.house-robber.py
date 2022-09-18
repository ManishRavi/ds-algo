#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start

# * Iterative Bottom-Up Solution | O(n) Time | O(1) Space
# * n -> The length of nums array


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = rob2 = 0
        for num in nums:
            rob1, rob2 = rob2, max(num + rob1, rob2)

        return rob2


# @lc code=end
