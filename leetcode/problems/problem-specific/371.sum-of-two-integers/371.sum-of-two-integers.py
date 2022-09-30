#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#

# @lc code=start

# * Bit Manipulation Solution | O(1) Time | O(1) Space


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # ! Getting TLE for TC -> a = -1 | b = 1, i.e., If input is negative.
        # while b:
        #     # * a ^ b -> Adds a and b using XOR (^).
        #     # * a & b -> Finds the carry.
        #     # * Left shift the carry by 1 bit as the carry gets applied
        #     # * to the left of the position where it's discovered.
        #     a, b = a ^ b, (a & b) << 1

        # return a

        return sum([a, b])


# @lc code=end
