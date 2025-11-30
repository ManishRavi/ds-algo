#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start

# * Iterative Bottom-Up Solution | O(n^3) Time | O(n^2) Space
# * n -> The length of nums array


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        nums_len = len(nums)
        dp = [[0] * (nums_len) for _ in range(nums_len)]
        max_coins = 0
        for left in range(nums_len - 2, 0, -1):
            for right in range(1, nums_len - 1):
                if left <= right:
                    for i in range(left, right + 1):
                        dp[left][right] = max(
                            dp[left][right],
                            nums[left - 1] * nums[i] * nums[right + 1]
                            + dp[left][i - 1]
                            + dp[i + 1][right],
                        )
                    max_coins = max(max_coins, dp[left][right])

        return max_coins


# @lc code=end
