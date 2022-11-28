#
# @lc app=leetcode id=446 lang=python3
#
# [446] Arithmetic Slices II - Subsequence
#

# @lc code=start

# * Iterative Bottom-Up Solution | O(n^2) Time | O(n^2) Space
# * n -> The length of nums array


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        nums_len = len(nums)
        dp = [collections.defaultdict(int) for _ in range(nums_len)]
        res = 0
        for i in range(nums_len):
            for j in range(i):
                sum_diff = nums[j] - nums[i]
                j_count = dp[j][sum_diff]
                dp[i][sum_diff] += 1 + j_count
                res += j_count

        return res


# @lc code=end
