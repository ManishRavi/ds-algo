#
# @lc app=leetcode id=1662 lang=python3
#
# [1662] Check If Two String Arrays are Equivalent
#

# @lc code=start

# * Two Pointers Solution | O(min(m, n)) Time | O(1) Space
# * m -> The length of word1 array | n -> The length of word2 array


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        def arrayStringsAreEqualGenerator(words):
            for word in words:
                for char in word:
                    yield char

            yield ""

        for char1, char2 in zip(
            arrayStringsAreEqualGenerator(word1), arrayStringsAreEqualGenerator(word2)
        ):
            if char1 != char2:
                return False

        return True


# @lc code=end
