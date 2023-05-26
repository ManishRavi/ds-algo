#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#

# @lc code=start

# * Iterative Top-Down Solution | O(mn) Time | O(mn) Space
# * m -> The length of s string | t -> The length of t string


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s_len, t_len = len(s), len(t)
        if t_len > s_len:
            return 0

        dp = [[0] * (t_len + 1) for _ in range(s_len + 1)]
        for i in range(s_len + 1):
            dp[i][0] = 1

        for i in range(1, s_len + 1):
            for j in range(1, t_len + 1):
                dp[i][j] = dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[s_len][t_len]


# @lc code=end
