#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start

# * Hash Table Solution | O(n) Time | O(n) Space
# * n -> The length of s or pattern string


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words) or len(set(pattern)) != len(set(words)):
            return False

        char_word_map = {}
        for char, word in zip(pattern, words):
            if char in char_word_map and char_word_map[char] != word:
                return False

            char_word_map[char] = word

        return True


# @lc code=end
