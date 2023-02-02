#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#

# @lc code=start

# * Iterative Math Solution | O(min(m, n)*(m + n)) Time | O(m + n) Space
# * m -> The length of str1 string | n -> The length of str2 string


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) < len(str1):
            str1, str2 = str2, str1

        str1_len, str2_len = len(str1), len(str2)

        def is_valid(i):
            if str1_len % i or str2_len % i:
                return False

            factor1, factor2 = str1_len // i, str2_len // i
            base = str1[:i]
            return base * factor1 == str1 and base * factor2 == str2

        for i in range(str1_len, 0, -1):
            if is_valid(i):
                return str1[:i]

        return ""


# @lc code=end
