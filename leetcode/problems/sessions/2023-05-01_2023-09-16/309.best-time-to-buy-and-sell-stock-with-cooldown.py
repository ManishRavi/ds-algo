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

        def dfs(start_idx, can_buy):
            if start_idx >= len(prices):
                return 0
            if (start_idx, can_buy) in memcache:
                return memcache[(start_idx, can_buy)]

            cooldown_val = dfs(start_idx + 1, can_buy)
            if can_buy:
                buy_val = dfs(start_idx + 1, not can_buy) - prices[start_idx]
                memcache[(start_idx, can_buy)] = max(buy_val, cooldown_val)
            else:
                sell_val = dfs(start_idx + 2, not can_buy) + prices[start_idx]
                memcache[(start_idx, can_buy)] = max(sell_val, cooldown_val)

            return memcache[(start_idx, can_buy)]

        return dfs(0, True)


# @lc code=end
