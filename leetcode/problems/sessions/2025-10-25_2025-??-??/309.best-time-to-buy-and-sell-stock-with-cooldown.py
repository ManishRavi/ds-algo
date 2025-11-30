#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start

# * Recursive Top-Down Solution | O(n) Time | O(n) Space
# * n -> The length of prices array


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memcache = {}

        def helper(start_idx, can_buy):
            if start_idx >= len(prices):
                return 0
            if (start_idx, can_buy) in memcache:
                return memcache[(start_idx, can_buy)]

            cooldown_profit = helper(start_idx + 1, can_buy)
            buy_or_sell_profit = 0
            if can_buy:
                buy_or_sell_profit = (
                    helper(start_idx + 1, not can_buy) - prices[start_idx]
                )
            else:
                buy_or_sell_profit = (
                    helper(start_idx + 2, not can_buy) + prices[start_idx]
                )

            memcache[(start_idx, can_buy)] = max(buy_or_sell_profit, cooldown_profit)
            return memcache[(start_idx, can_buy)]

        return helper(0, True)


# @lc code=end
