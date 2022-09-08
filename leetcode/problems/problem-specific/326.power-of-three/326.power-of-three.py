#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start

# * Bit Manipulation Solution | O(1) Time | O(1) Space


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # * Any integer number other than the power of 3 which divides the highest
        # * power of 3 value that integer can hold 3^19 = 1162261467 (Assuming that
        # * integers are stored using 32 bits) will give reminder non-zero.
        return n > 0 and not (1162261467 % n)


# @lc code=end
