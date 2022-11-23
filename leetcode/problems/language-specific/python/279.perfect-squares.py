#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start

# * Iterative Bottom-Up Solution | O(mn) Time | O(n) Space
# * m -> The perfect squares array | n -> The given input


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n + 1] * (n + 1)
        dp[0] = 0
        for num in range(1, n + 1):
            num *= num
            for t in range(num, n + 1):
                dp[t] = min(dp[t], 1 + dp[t - num])

        return dp[n]


# @lc code=end
