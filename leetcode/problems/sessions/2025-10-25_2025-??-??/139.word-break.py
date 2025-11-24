#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start

# * Iterative Bottom-Up Solution | O((n^2)*m) Time | O(n) Space
# * n -> The length of s string | m -> The length of wordDict array


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s_len = len(s)
        dp = [False] * (s_len + 1)
        dp[s_len] = True

        for i in range(s_len - 1, -1, -1):
            for word in wordDict:
                if s[i : i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break

        return dp[0]


# @lc code=end
