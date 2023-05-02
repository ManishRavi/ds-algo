#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start

# * Hash Table Solution | O(n) Time | O(n) Space
# * n -> The length of s or t string


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len, t_len = len(s), len(t)
        if s_len != t_len:
            return False

        s_counter = Counter(s)
        for char in t:
            s_counter[char] -= 1
            if s_counter[char] < 0:
                return False

        return True


# @lc code=end
