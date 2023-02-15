#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start

# * Math Solution | O(max(m, n)) Time | O(1) Space
# * m -> The length of a string | n -> The length of b string


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        m, n = len(a) - 1, len(b) - 1
        carry = 0
        while m >= 0 or n >= 0 or carry > 0:
            val1 = ord(a[m]) - ord("0") if m >= 0 else 0
            val2 = ord(b[n]) - ord("0") if n >= 0 else 0
            carry += val1 + val2
            res.append(str(carry % 2))
            carry //= 2

            m -= 1
            n -= 1

        res.reverse()
        return "".join(res)


# @lc code=end
