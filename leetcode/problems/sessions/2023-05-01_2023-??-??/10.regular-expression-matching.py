#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start

# * Recursive Top-Down Solution | O(mn) Time | O(mn) Space
# * m -> The length of s string | n -> The length of p string


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        memcache = {}

        def dfs(s_idx, p_idx):
            if s_idx >= s_len and p_idx >= p_len:
                return True
            if p_idx >= p_len:
                return False
            if (s_idx, p_idx) in memcache:
                return memcache[(s_idx, p_idx)]

            is_match = s_idx < s_len and (s[s_idx] == p[p_idx] or p[p_idx] == ".")
            if p_idx + 1 < p_len and p[p_idx + 1] == "*":
                memcache[(s_idx, p_idx)] = dfs(s_idx, p_idx + 2) or (
                    is_match and dfs(s_idx + 1, p_idx)
                )
            elif is_match:
                memcache[(s_idx, p_idx)] = dfs(s_idx + 1, p_idx + 1)
            else:
                memcache[(s_idx, p_idx)] = False

            return memcache[(s_idx, p_idx)]

        return dfs(0, 0)


# @lc code=end
