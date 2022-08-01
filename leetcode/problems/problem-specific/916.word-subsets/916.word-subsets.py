#
# @lc app=leetcode id=916 lang=python3
#
# [916] Word Subsets
#

# @lc code=start

# * HashTable Solution | O(m+n) Time | O(m+n) Space
# * m -> Number of words in words1 | n -> Number of words in words2

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def get_count(word):
            counter = [0]*26
            for letter in word:
                counter[ord(letter)-ord('a')] += 1

            return counter

        words2_counter = [0]*26
        for word2 in words2:
            for i, c in enumerate(get_count(word2)):
                words2_counter[i] = max(words2_counter[i], c)

        universal_strings = []
        for word1 in words1:
            words1_counter = get_count(word1)
            for i in range(len(words1_counter)):
                if words1_counter[i] < words2_counter[i]:
                    break

            else:
                universal_strings.append(word1)

        return universal_strings

# @lc code=end
