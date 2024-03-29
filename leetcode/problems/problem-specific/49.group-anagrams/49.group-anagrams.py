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
        res = collections.defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for char in s:
                counts[ord(char) - ord("a")] += 1
            res[tuple(counts)].append(s)

        return res.values()


# @lc code=end
