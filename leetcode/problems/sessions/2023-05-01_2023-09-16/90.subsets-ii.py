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
        res = []
        nums.sort()

        def helper(start_idx, subset):
            res.append(subset[:])

            for i in range(start_idx, len(nums)):
                if i > start_idx and nums[i] == nums[i - 1]:
                    continue

                helper(i + 1, subset + [nums[i]])

        helper(0, [])
        return res


# @lc code=end
