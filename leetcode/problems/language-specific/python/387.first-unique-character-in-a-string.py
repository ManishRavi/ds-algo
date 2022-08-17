#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start

# * Hash Table Solution | O(n) Time | O(1) Space
# * n -> The length of s string

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # * Contains only 26 lowercase letters which makes it a constant space
        s_counter = collections.Counter(s)
        for idx, c in enumerate(s):
            if s_counter[c] == 1:
                return idx

        return -1

# @lc code=end
