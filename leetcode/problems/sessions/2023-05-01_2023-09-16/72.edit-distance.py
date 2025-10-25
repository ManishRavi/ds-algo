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
        for j in range(word2_len + 1):
            dp[0][j] = j
        for i in range(word1_len + 1):
            dp[i][0] = i

        for i in range(1, word1_len + 1):
            for j in range(1, word2_len + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])

        return dp[word1_len][word2_len]


# @lc code=end
