#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start

# * Math Solution | O(n) Time | O(1) Space
# * n -> The given input x


class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT = -2147483648  # * -2^31
        MAX_INT = 2147483647  # * 2^31 - 1
        res, n = 0, abs(x)
        while n:
            res *= 10
            res += n % 10
            n //= 10

        if x < 0:
            res = -res
        if res < MIN_INT or res > MAX_INT:
            return 0

        return res


# @lc code=end
