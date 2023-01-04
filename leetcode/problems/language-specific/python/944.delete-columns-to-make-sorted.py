#
# @lc app=leetcode id=944 lang=python3
#
# [944] Delete Columns to Make Sorted
#

# @lc code=start

# * Iterative Solution | O(nl) Time | O(1) Space
# * n -> The length of strs array | l -> The length of each string


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        for i in range(len(strs[0])):
            for j in range(len(strs) - 1):
                if strs[j][i] > strs[j + 1][i]:
                    res += 1
                    break

        return res


# @lc code=end
