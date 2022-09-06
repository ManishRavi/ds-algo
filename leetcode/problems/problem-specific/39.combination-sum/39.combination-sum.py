#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start

# * Backtracking Solution | O(n*(2^t)) Time | O(n) Space
# * n -> The length of candidates array | t -> Given target

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def combinationSumHelper(start=0, target=target, combination=[]):
            if target < 0:
                return
            if target == 0:
                result.append(combination[:])
                return

            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                combinationSumHelper(i, target - candidates[i], combination)
                combination.pop()

        combinationSumHelper()
        return result

# @lc code=end
