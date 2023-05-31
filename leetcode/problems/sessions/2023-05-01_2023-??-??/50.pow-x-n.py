#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start

# * Math Solution | O(logn) Time | O(1) Space
# * n -> The given input


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        if n < 0:
            return self.myPow(1 / x, -n)
        elif n % 2 == 0:
            return self.myPow(x * x, n // 2)

        return x * self.myPow(x * x, n // 2)


# @lc code=end
