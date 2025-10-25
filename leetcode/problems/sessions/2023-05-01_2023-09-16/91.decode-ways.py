#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start

# * Recursive Top-Down Solution | O(n) Time | O(n) Space
# * n -> The length of s string


class Solution:
    def numDecodings(self, s: str) -> int:
        s_len = len(s)
        memcache = [0] * (s_len + 1)

        def dfs(start_idx):
            if start_idx == s_len:
                return 1
            if s[start_idx] == "0":
                return 0
            if memcache[start_idx]:
                return memcache[start_idx]

            res = dfs(start_idx + 1)
            if start_idx + 1 < s_len and int(s[start_idx : start_idx + 2]) <= 26:
                res += dfs(start_idx + 2)

            memcache[start_idx] = res
            return memcache[start_idx]

        return dfs(0)


# @lc code=end
