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
        s_length = len(s)
        ROMAN_SYMBOLS = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = 0
        i = 0
        while i < s_length-1:
            cur_val, next_val = ROMAN_SYMBOLS[s[i]], ROMAN_SYMBOLS[s[i+1]]
            if next_val > cur_val:
                result += next_val - cur_val
                i += 1

            else:
                result += cur_val

            i += 1

        return result if i == s_length else result+ROMAN_SYMBOLS[s[i]]

# @lc code=end
