#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start

# * Iterative Bottom-Up Solution | O(mn) Time | O(mn) Space
# * m -> The length of text1 string | n -> The length of text2 string


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1_len, text2_len = len(text1), len(text2)
        # * Create a 2-D DP with the rows as text1_len + 1 (Including empty string)
        # * and cols as text2_len + 1 (Including empty string).
        dp = [[0] * (text2_len + 1) for _ in range(text1_len + 1)]
        # * Start the iteration from the first row and first col.
        for i in range(1, text1_len + 1):
            for j in range(1, text2_len + 1):
                # * If both chars match then we set the value by chopping
                # * the current char in both the strings and adding 1 to it.
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                # * Else we take the max between chopping the current char in text1 or text2.
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[text1_len][text2_len]


# @lc code=end
