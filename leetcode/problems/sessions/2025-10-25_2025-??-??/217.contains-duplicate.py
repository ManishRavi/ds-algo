#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start

# * Hash Table Solution | O(n) Time | O(n) Space
# * n -> The length of nums array


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_idx_map = {}
        for idx, num in enumerate(nums):
            if num in num_idx_map:
                return True

            num_idx_map[num] = idx

        return False


# @lc code=end
