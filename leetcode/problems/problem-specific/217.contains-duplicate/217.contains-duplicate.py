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
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True

            nums_set.add(num)

        return False

# @lc code=end
