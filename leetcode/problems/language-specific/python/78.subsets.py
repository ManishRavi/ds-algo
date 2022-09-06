#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start

# * Backtracking Solution | O(n*(2^n)) Time | O(n) Space
# * n -> The length of nums array

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def subsetsHelper(start=0, subset=[]):
            result.append(subset[:])

            for i in range(start, len(nums)):
                subset.append(nums[i])
                subsetsHelper(i + 1, subset)
                subset.pop()

        subsetsHelper()
        return result

# @lc code=end
