#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#

# @lc code=start

# * Iterative Bottom-Up Solution | O(ca) Time | O(a) Space
# * c -> The length of coins array | a -> The given input amount


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for a in range(c, amount + 1):
                dp[a] += dp[a - c]

        return dp[amount]


# @lc code=end
