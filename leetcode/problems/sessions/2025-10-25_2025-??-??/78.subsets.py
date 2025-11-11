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
        res = []

        def helper(start_idx, subset):
            res.append(subset[:])

            for i in range(start_idx, len(nums)):
                subset.append(nums[i])
                helper(i + 1, subset)
                subset.pop()

        helper(0, [])
        return res


# @lc code=end
