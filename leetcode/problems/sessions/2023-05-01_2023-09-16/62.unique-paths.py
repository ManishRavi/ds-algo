#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start

# * Iterative Bottom-Up Solution | O(mn) Time | O(n) Space
# * m -> The given input | n -> The given input


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for col in range(1, n):
                dp[col] += dp[col - 1]

        return dp[n - 1]


# @lc code=end
