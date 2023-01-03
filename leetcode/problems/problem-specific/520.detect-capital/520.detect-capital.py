#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#

# @lc code=start

# * Counting Solution | O(n) Time | O(1) Space
# * n -> The length of word string


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()


# @lc code=end
