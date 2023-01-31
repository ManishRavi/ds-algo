#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start

# * Iterative Solution | O(n) Time | O(1) Space
# * n -> The given input


class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n

        a, b, c = 0, 1, 1
        for i in range(3, n + 1):
            a, b, c = b, c, a + b + c

        return c


# @lc code=end
