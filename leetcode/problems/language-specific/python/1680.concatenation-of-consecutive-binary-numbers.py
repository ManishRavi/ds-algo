#
# @lc app=leetcode id=1680 lang=python3
#
# [1680] Concatenation of Consecutive Binary Numbers
#

# @lc code=start

# * Bit Manipulation Solution | O(n) Time | O(1) Space
# * n -> The given input


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return int("".join([bin(i)[2:] for i in range(1, n + 1)]), 2) % (10**9 + 7)


# @lc code=end
