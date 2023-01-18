#
# @lc app=leetcode id=926 lang=python3
#
# [926] Flip String to Monotone Increasing
#

# @lc code=start

# * Counting Solution | O(n) Time | O(1) Space
# * n -> The length of s string


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        res = no_of_ones = 0
        for char in s:
            if char == "1":
                no_of_ones += 1
            else:
                res = min(1 + res, no_of_ones)

        return res


# @lc code=end
