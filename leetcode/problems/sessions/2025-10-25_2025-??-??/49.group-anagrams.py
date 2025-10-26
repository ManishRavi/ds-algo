#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start

# * Hash Table Solution | O(mn) Time | O(n) Space
# * m -> The length of strs array | n -> The length of each string


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            word_counter = [0] * 26
            for char in word:
                word_counter[ord(char) - ord("a")] += 1
            res[tuple(word_counter)].append(word)

        return list(res.values())


# @lc code=end
