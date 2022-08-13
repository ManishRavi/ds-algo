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
        index_mappings = {}
        for idx, num in enumerate(nums):
            other_val = target - num
            if other_val in index_mappings:
                return [index_mappings[other_val], idx]

            index_mappings[num] = idx

# @lc code=end
