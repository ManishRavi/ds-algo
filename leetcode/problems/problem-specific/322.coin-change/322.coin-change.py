#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start

# * Iterative Bottom-Up Solution | O(ca) Time | O(a) Space
# * c -> The length of coins array | a -> The given input amount


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for c in coins:
            for a in range(c, amount + 1):
                dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != amount + 1 else -1


# @lc code=end
