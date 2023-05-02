#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc code=start

# * Hash Table Solution | O(n) Time | O(n) Space
# * n -> The length of nums array


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx_map = {}
        for idx, num in enumerate(nums):
            other_val = target - num
            if other_val in num_idx_map:
                return [num_idx_map[other_val], idx]

            num_idx_map[num] = idx


# @lc code=end
