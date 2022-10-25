#
# @lc app=leetcode id=1239 lang=python3
#
# [1239] Maximum Length of a Concatenated String with Unique Characters
#

# @lc code=start

# * Backtracking Solution | O(m*(2^n)) Time | O(n) Space
# * n -> The length of arr array | m -> The length of each string


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        max_len = 0

        def maxLengthHelper(start_idx, subset):
            nonlocal max_len

            cur_val = "".join([s for s in subset])
            if len(set(cur_val)) == len(cur_val):
                max_len = max(max_len, len(set(cur_val)))

            for i in range(start_idx, len(arr)):
                subset.append(arr[i])
                maxLengthHelper(i + 1, subset)
                subset.pop()

        maxLengthHelper(0, [])
        return max_len


# @lc code=end
