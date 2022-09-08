#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start

# * Bit Manipulation Solution | O(1) Time | O(1) Space
# * The given number n is a power of 4 if it's
# * a power of 2 and its only set bit is present at even position (0, 2, 4, ...).


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # * n & (n - 1) -> To check if the number is a power of 2.
        # * n & 0xAAAAAAAA -> To check the position of its set bit, we can use 0xAAAAAAAA as a mask.
        # * The mask 0xAAAAAAAA has 1 in all its odd position.
        # * So if the expression !(n & 0xAAAAAAAA) is true, the position of the set bit in n is even.
        return n and not (n & (n - 1)) and not (n & 0xAAAAAAAA)


# @lc code=end
