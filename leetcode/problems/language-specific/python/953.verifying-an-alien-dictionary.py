#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start

# * Hash Table Solution | O(nl) Time | O(l) Space
# * n -> The length of words array | l -> The length of each word


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        words_len = len(words)
        char_idx_map = {char: idx for idx, char in enumerate(order)}
        for i in range(words_len - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))
            if word1[:min_len] == word2[:min_len] and len(word1) > len(word2):
                return False

            for i in range(min_len):
                if word1[i] != word2[i]:
                    if char_idx_map[word1[i]] > char_idx_map[word2[i]]:
                        return False

                    break

        return True


# @lc code=end
