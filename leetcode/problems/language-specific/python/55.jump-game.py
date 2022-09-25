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
        # * Stores the max index that we can reach using the max jumps at each and every index.
        farthest_reached_idx = 0
        for idx, num in enumerate(nums):
            # * Break if the current index ever reaches a point where we can't jump or
            # * we've reached the last index even before we iterate the complete array.
            if idx > farthest_reached_idx or farthest_reached_idx >= nums_len - 1:
                break

            farthest_reached_idx = max(farthest_reached_idx, idx + num)

        return True if farthest_reached_idx >= nums_len - 1 else False


# @lc code=end
