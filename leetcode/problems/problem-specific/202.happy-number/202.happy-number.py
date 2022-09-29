#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start

# * Floyd's Tortoise and Hare Cycle Detection Solution | O(logn) Time | O(1) Space
# * n -> The given input


class Solution:
    def isHappy(self, n: int) -> bool:
        slow = fast = n
        while True:
            slow = self._sum_digits_squares(slow)
            fast = self._sum_digits_squares(self._sum_digits_squares(fast))
            if slow == fast:
                break

        return slow == 1

    def _sum_digits_squares(self, num):
        res = 0
        while num:
            res += (num % 10) ** 2
            num //= 10

        return res


# @lc code=end
