#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start

# * Iterative Bottom-Up Solution | O(mn) Time | O(mn) Space
# * m -> The length of word1 string | n -> The length of word2 string


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1_len, word2_len = len(word1), len(word2)
        dp = [[0] * (word2_len + 1) for _ in range(word1_len + 1)]
        for col in range(word2_len + 1):
            dp[0][col] = col
        for row in range(word1_len + 1):
            dp[row][0] = row

        for row in range(1, word1_len + 1):
            for col in range(1, word2_len + 1):
                if word1[row - 1] == word2[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1]
                else:
                    dp[row][col] = 1 + min(
                        dp[row - 1][col], dp[row - 1][col - 1], dp[row][col - 1]
                    )

        return dp[word1_len][word2_len]


# @lc code=end
