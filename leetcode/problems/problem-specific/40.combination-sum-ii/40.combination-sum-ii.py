#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start

# * Backtracking Solution | O(n*(2^t)) Time | O(n) Space
# * n -> The length of candidates array | t -> Given target

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def combinationSum2Helper(start=0, target=target, combination=[]):
            if target < 0:
                return
            if target == 0:
                result.append(combination[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                combination.append(candidates[i])
                combinationSum2Helper(i + 1, target - candidates[i], combination)
                combination.pop()

        combinationSum2Helper()
        return result

# @lc code=end
