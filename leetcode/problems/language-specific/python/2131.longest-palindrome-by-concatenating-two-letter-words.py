#
# @lc app=leetcode id=2131 lang=python3
#
# [2131] Longest Palindrome by Concatenating Two Letter Words
#

# @lc code=start

# * Hash Table Solution | O(n) Time | O(n) Space
# * n -> The length of words array


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        words_counter = collections.Counter(words)
        res = center = 0
        for word, word_count in words_counter.items():
            reversed_word = word[::-1]
            if word == reversed_word:
                if word_count % 2 == 0:
                    res += word_count
                else:
                    res += word_count - 1
                    center = 2
            else:
                res += min(word_count, words_counter[reversed_word])

        return res * 2 + center


# @lc code=end
