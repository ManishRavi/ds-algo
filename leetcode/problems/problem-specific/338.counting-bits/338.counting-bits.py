#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start

# * Bit Manipulation Solution | O(n) Time | O(1) Space
# * n -> The given input


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            # * For even number -> # of 1s in i will be # of 1s in (i/2) or (i>>1).
            # * For odd number -> # of 1s in i will be # of 1s in (i/2) or (i>>1) + 1.
            res[i] = res[i >> 1] + (i % 2)

        return res


# @lc code=end
