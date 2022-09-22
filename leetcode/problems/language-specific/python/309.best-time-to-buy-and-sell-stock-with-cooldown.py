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
        # * Stores a key-value pair where the key is a pair of start
        # * index & buy/sell state and value is the max profit.
        # * Key -> (start_idx, can_buy) | Value -> max_profit
        memcache = {}

        def maxProfitHelper(start_idx, can_buy):
            if start_idx >= len(prices):
                return 0
            if (start_idx, can_buy) in memcache:
                return memcache[(start_idx, can_buy)]

            cooldown_val = maxProfitHelper(start_idx + 1, can_buy)
            # * If we can buy the stock.
            if can_buy:
                buy_val = (
                    maxProfitHelper(start_idx + 1, not can_buy) - prices[start_idx]
                )
                memcache[(start_idx, can_buy)] = max(buy_val, cooldown_val)
            # * If we need to sell the stock to make a profit.
            else:
                # * Move the start_idx to start_idx + 2 after we sell the stock as we need
                # * to cooldown before buying the new stock, i.e., skip the next element.
                sell_val = (
                    maxProfitHelper(start_idx + 2, not can_buy) + prices[start_idx]
                )
                memcache[(start_idx, can_buy)] = max(sell_val, cooldown_val)

            return memcache[(start_idx, can_buy)]

        return maxProfitHelper(0, True)


# @lc code=end
