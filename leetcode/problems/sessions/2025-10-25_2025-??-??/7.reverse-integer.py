#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start

# * Math Solution | O(n) Time | O(1) Space
# * n -> The number of digits in the x


class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT, MAX_INT = -(2**31), (2**31) - 1
        n = abs(x)
        res = 0
        while n:
            res *= 10
            res += n % 10
            n //= 10

        if x < 0:
            res = -res
        if not MIN_INT <= res <= MAX_INT:
            return 0

        return res


# @lc code=end
