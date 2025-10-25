#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start

# * Greedy Solution | O(n) Time | O(1) Space
# * n -> The length of nums array


class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jumps = farthest_reached_idx = end_idx = 0
        for idx, num in enumerate(nums[:-1]):
            farthest_reached_idx = max(farthest_reached_idx, idx + num)
            if idx == end_idx:
                end_idx = farthest_reached_idx
                min_jumps += 1

        return min_jumps


# @lc code=end
