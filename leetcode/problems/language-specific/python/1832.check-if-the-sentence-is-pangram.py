#
# @lc app=leetcode id=1832 lang=python3
#
# [1832] Check if the Sentence Is Pangram
#

# @lc code=start

# * Hash Table Solution | O(n) Time | O(1) Space
# * n -> The length of sentence string


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        char_set = set(sentence)
        return len(char_set) == 26


# @lc code=end
