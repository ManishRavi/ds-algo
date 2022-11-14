#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start

# * Easy Solution | O(n) Time | O(n) Space
# * n -> The length of s string


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


# @lc code=end
