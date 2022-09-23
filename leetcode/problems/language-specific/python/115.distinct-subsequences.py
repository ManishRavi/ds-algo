#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#

# @lc code=start

# * Iterative Bottom-Up Solution | O(mn) Time | O(mn) Space
# * m -> The length of s string | n -> The length of t string


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s_len, t_len = len(s), len(t)
        if t_len > s_len:
            return 0

        # * Create a 2-D DP with the rows as s_len + 1 (Including empty string)
        # * and cols as t_len + 1 (Including empty string).
        dp = [[0] * (t_len + 1) for _ in range(s_len + 1)]
        # * Set the first col to 1 as we can always have 1 way if t is empty.
        for i in range(s_len + 1):
            dp[i][0] = 1

        # * Start the iteration from the first row and first col.
        for i in range(1, s_len + 1):
            for j in range(1, t_len + 1):
                # * This handles both the chars mismatch and chars match cases where
                # * we need the no. of ways by chopping the current char.
                dp[i][j] = dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    # * If both chars match then we set the value by chopping the current
                    # * char in both strings and adding it to the previous result.
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[s_len][t_len]


# @lc code=end
