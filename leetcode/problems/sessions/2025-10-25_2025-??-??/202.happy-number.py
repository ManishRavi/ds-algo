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
            slow = self.get_sum_digits_squares(slow)
            fast = self.get_sum_digits_squares(self.get_sum_digits_squares(fast))
            if slow == fast:
                break

        return slow == 1

    def get_sum_digits_squares(self, n):
        res = 0
        while n:
            res += (n % 10) ** 2
            n //= 10

        return res


# @lc code=end
