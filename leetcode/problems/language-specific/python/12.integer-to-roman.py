#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start

# * Math Solution | O(n) Time | O(1) Space
# * n -> The given input num


class Solution:
    def intToRoman(self, num: int) -> str:
        ROMAN_DIGITS = [
            ["M", 1000],
            ["CM", 900],
            ["D", 500],
            ["CD", 400],
            ["C", 100],
            ["XC", 90],
            ["L", 50],
            ["XL", 40],
            ["X", 10],
            ["IX", 9],
            ["V", 5],
            ["IV", 4],
            ["I", 1],
        ]

        res = []
        for val in ROMAN_DIGITS:
            while num >= val[1]:
                res.append(val[0])
                num -= val[1]
            if not num:
                return "".join(res)


# @lc code=end
