#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start

# * Backtracking Solution | O(n*(2^t)) Time | O(n) Space
# * n -> The length of candidates array | t -> The given input target


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(start_idx, target, combination):
            if target < 0:
                return
            if target == 0:
                res.append(combination[:])
                return

            for i in range(start_idx, len(candidates)):
                combination.append(candidates[i])
                helper(i, target - candidates[i], combination)
                combination.pop()

        helper(0, target, [])
        return res


# @lc code=end
