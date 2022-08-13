#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start

# * Hash Table Solution | O(n) Time | O(n) Space
# * n -> The length of s or t

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        t_counter = collections.Counter(t)
        for c in s:
            t_counter[c] -= 1
            if t_counter[c] < 0:
                return False

        return True

# @lc code=end
