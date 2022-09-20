#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start

# * Binary Search Solution | O(nlogn) Time | O(n) Space
# * n -> The length of nums array


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # * Stores the elements in ascending order so as to apply the binary search.
        # * Final result might not contain the longest subsequence values
        # * as we're overwriting the values to save space.
        res = []
        for num in nums:
            if not res or num > res[-1]:
                res.append(num)
            else:
                insert_idx = bisect.bisect_left(res, num)
                res[insert_idx] = num

        return len(res)


# @lc code=end
