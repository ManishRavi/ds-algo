#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start

# * Backtracking Solution | O(n*(2^n)) Time | O(n) Space
# * n -> The length of nums array

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def subsetsWithDupHelper(start=0, subset=[]):
            result.append(subset[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])
                subsetsWithDupHelper(i + 1, subset)
                subset.pop()

        subsetsWithDupHelper()
        return result

# @lc code=end
