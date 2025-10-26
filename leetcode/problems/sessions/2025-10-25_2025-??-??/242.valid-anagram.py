#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start

# * Hash Table Solution | O(n) Time | O(n) Space
# * n -> The max length of strings s or t


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        t_counter = Counter(t)
        for char in s:
            t_counter[char] -= 1
            if t_counter[char] < 0:
                return False

        return True


# @lc code=end
