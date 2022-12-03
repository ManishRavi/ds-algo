#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#

# @lc code=start

# * Counting and Hash Table Solution | O(n) Time | O(n) Space
# * n -> The length of word1 string


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False

        word1_counter = Counter(word1)
        word2_counter = Counter(word2)
        return Counter(word1_counter.values()) == Counter(word2_counter.values())


# @lc code=end
