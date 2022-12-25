#
# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#

# @lc code=start

# * Iterative Bottom-Up Solution | O(n) Time | O(n) Space
# * n -> The given input


class Solution:
    def numTilings(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1], dp[2], dp[3] = 1, 2, 5
        for i in range(4, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % (10**9 + 7)

        return dp[n]


# @lc code=end
