#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start

# * Hash Table Solution | O(n) Time | O(1) Space
# * n -> The length of s string


class Solution:
    def romanToInt(self, s: str) -> int:
        s_len = len(s)
        ROMAN_DIGIT_MAP = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        res = 0
        i = 0
        while i < s_len - 1:
            cur_val, next_val = ROMAN_DIGIT_MAP[s[i]], ROMAN_DIGIT_MAP[s[i + 1]]
            if next_val > cur_val:
                res += next_val - cur_val
                i += 1
            else:
                res += cur_val
            i += 1

        return res if i == s_len else res + ROMAN_DIGIT_MAP[s[i]]


# @lc code=end
