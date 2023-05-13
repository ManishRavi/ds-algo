#
# @lc app=leetcode id=2140 lang=python3
#
# [2140] Solving Questions With Brainpower
#

# @lc code=start

# * Recursive Top-Down Solution | O(n) Time | O(n) Space
# * n -> The length of questions array


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = {}

        def dfs(i):
            if i >= len(questions):
                return 0
            if i in dp:
                return dp[i]

            dp[i] = max(dfs(i + 1), questions[i][0] + dfs(i + 1 + questions[i][1]))
            return dp[i]

        return dfs(0)


# @lc code=end
