#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start

# * Math Solution | O(n) Time | O(1) Space
# * n -> The number of digits in the given input x


class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT, MAX_INT = -(2**31), (2**31 - 1)
        res, n = 0, abs(x)
        while n:
            res = (res * 10) + (n % 10)
            n //= 10

        if x < 0:
            res = -res

        return res if MIN_INT <= res <= MAX_INT else 0


# @lc code=end
