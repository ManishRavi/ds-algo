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
        dp = [[0] * (text2_len + 1) for _ in range(text1_len + 1)]
        for row in range(1, text1_len + 1):
            for col in range(1, text2_len + 1):
                if text1[row - 1] == text2[col - 1]:
                    dp[row][col] = 1 + dp[row - 1][col - 1]
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

        return dp[text1_len][text2_len]


# @lc code=end
