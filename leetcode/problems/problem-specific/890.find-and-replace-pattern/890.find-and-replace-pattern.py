#
# @lc app=leetcode id=890 lang=python3
#
# [890] Find and Replace Pattern
#

# @lc code=start

# * HashMap Solution | O(nk) Time | O(nk) Space
# * n -> Number of words | k -> Length of each word

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            mappings = {}
            for p, w in zip(pattern, word):
                if mappings.setdefault(p, w) != w:
                    return False

            return len(set(mappings.values())) == len(mappings.values())

        return filter(match, words)

# @lc code=end
