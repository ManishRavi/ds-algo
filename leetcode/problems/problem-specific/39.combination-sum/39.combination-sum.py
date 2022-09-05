#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start

# * Backtracking Solution | O(n*(2^n)) Time | O(n) Space
# * n -> The number of nums array

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def combinationSumHelper(index=0, total=0, combination=[]):
            if total == target:
                result.append(combination[:])
                return

            if index >= len(candidates) or total > target:
                return

            # * Include candidates[index]
            combination.append(candidates[index])
            combinationSumHelper(index, total + candidates[index], combination)
            # * Don't include candidates[index]
            combination.pop()
            combinationSumHelper(index + 1, total, combination)

        combinationSumHelper()
        return result

# @lc code=end
