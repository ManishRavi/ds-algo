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
        # * Create a 2-D DP with the rows as word1_len + 1 (Including empty string)
        # * and cols as word2_len + 1 (Including empty string).
        dp = [[0] * (word2_len + 1) for _ in range(word1_len + 1)]
        # * Fill the first row.
        for j in range(word2_len + 1):
            dp[0][j] = j
        # * Fill the first column.
        for i in range(word1_len + 1):
            dp[i][0] = i

        # * Start the iteration from the first row and first col.
        for i in range(1, word1_len + 1):
            for j in range(1, word2_len + 1):
                # * If both chars match then we set the previous value
                # * by chopping the current char in both the strings.
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # * Else find the minimum of 3 operations and add 1 to it for the current action.
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])

        return dp[word1_len][word2_len]


# @lc code=end
