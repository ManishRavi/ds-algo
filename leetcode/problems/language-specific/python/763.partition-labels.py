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
        char_last_idx_map = collections.defaultdict()
        for idx, char in enumerate(s):
            char_last_idx_map[char] = idx

        res = []
        # * The left pointer will store the start index of the current partition and
        # * the right pointer will store the end index of the current partition.
        left = right = 0
        for idx, char in enumerate(s):
            right = max(right, char_last_idx_map[char])
            # * When the current index reaches the right pointer index, we can add the current window
            # * size to the result and move the left pointer to the next starting partition index.
            if idx == right:
                res.append(right - left + 1)
                left = right + 1

        return res


# @lc code=end
