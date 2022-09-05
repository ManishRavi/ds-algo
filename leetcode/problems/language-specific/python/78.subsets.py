#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start

# * Backtracking Solution | O(n*(2^n)) Time | O(n) Space
# * n -> The number of nums array

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def subsetsHelper(index=0, subset=[]):
            if index == len(nums):
                result.append(subset[:])
                return

            # * Include nums[index]
            subset.append(nums[index])
            subsetsHelper(index + 1, subset)
            # * Don't include nums[index]
            subset.pop()
            subsetsHelper(index + 1, subset)

        subsetsHelper()
        return result

# @lc code=end
