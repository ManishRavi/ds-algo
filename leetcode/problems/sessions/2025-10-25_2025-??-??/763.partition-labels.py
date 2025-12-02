#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start

# * Greedy and Two Pointers Solution | O(n) Time | O(1) Space
# * n -> The length of s string


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_to_last_idx_map = {}
        for idx, char in enumerate(s):
            char_to_last_idx_map[char] = idx

        res = []
        left = right = 0
        for idx, char in enumerate(s):
            right = max(right, char_to_last_idx_map[char])
            if idx == right:
                res.append(right - left + 1)
                left = right + 1

        return res


# @lc code=end
