#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start

# * Bit Manipulation Solution | O(logn) Time | O(1) Space
# * n -> The given input


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res


# @lc code=end
