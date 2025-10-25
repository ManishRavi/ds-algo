#
# @lc app=leetcode id=521 lang=python3
#
# [521] Longest Uncommon Subsequence I
#


# @lc code=start

# * Logical Solution | O(n) Time | O(1) Space
# * n -> The max length of a or b


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a), len(b))


# @lc code=end
