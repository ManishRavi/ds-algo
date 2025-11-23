#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start

# * Iterative Bottom-Up Solution | O(n) Time | O(1) Space
# * n -> The given input


class Solution:
    def climbStairs(self, n: int) -> int:
        step1 = step2 = 1
        for _ in range(2, n + 1):
            step1, step2 = step2, step1 + step2

        return step2


# @lc code=end
