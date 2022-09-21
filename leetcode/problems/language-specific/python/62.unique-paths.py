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
        # * Create a 1-D DP array with the size as n and the values as 1 since
        # * the first row and first col will have only 1 possible pathway.
        dp = [1] * n
        # * Start from the first row and go through all the cols except for the first one.
        for _ in range(1, m):
            for col in range(1, n):
                dp[col] += dp[col - 1]

        return dp[n - 1]


# @lc code=end
