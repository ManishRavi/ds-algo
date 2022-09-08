#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start

# * Backtracking Solution | O(n*(2^t)) Time | O(n) Space
# * n -> The length of candidates array | t -> The given input target


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def combinationSum2Helper(start_idx, target, combination):
            if target < 0:
                return
            if target == 0:
                res.append(combination[:])
                return

            for i in range(start_idx, len(candidates)):
                if i > start_idx and candidates[i] == candidates[i - 1]:
                    continue

                combination.append(candidates[i])
                combinationSum2Helper(i + 1, target - candidates[i], combination)
                combination.pop()

        combinationSum2Helper(0, target, [])
        return res


# @lc code=end
