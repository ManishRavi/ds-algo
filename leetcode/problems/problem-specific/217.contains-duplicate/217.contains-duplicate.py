#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start

# * Hash Table Solution | O(n) Time | O(n) Space
# * n -> Length of nums array

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return True

            hash_set.add(num)

        return False

# @lc code=end
