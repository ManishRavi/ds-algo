#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#

# @lc code=start

# * Recursive Top-Down Solution | O(mn) Time | O(mn) Space
# * m -> The length of s string | n -> The length of t string


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s_len, t_len = len(s), len(t)
        if t_len > s_len:
            return 0

        memcache = {}

        def helper(i, j):
            if j == t_len:
                return 1
            if i == s_len:
                return 0
            if (i, j) in memcache:
                return memcache[(i, j)]

            cur_ways = helper(i + 1, j)
            if s[i] == t[j]:
                cur_ways += helper(i + 1, j + 1)

            memcache[(i, j)] = cur_ways
            return memcache[(i, j)]

        return helper(0, 0)


# @lc code=end
