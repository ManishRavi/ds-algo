#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start

# * Greedy Solution | O(n) Time | O(1) Space
# * n -> The length of nums array


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        farthest_reached_idx = 0
        for idx, num in enumerate(nums):
            if idx > farthest_reached_idx or farthest_reached_idx >= nums_len - 1:
                break

            farthest_reached_idx = max(farthest_reached_idx, idx + num)

        return farthest_reached_idx >= nums_len - 1


# @lc code=end
