#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start

# * Recursive Bottom-Up Solution | O(n) Time | O(n) Space
# * n -> The length of prices array


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # * Stores a key-value pair where the key is a pair of start
        # * index and buy/sell state and value is the max profit.
        # * Key -> (start_idx, is_buying) | Value -> max_profit
        dp = {}

        def maxProfitHelper(start_idx, is_buying):
            if start_idx >= len(prices):
                return 0
            if (start_idx, is_buying) in dp:
                return dp[(start_idx, is_buying)]

            cooldown_val = maxProfitHelper(start_idx + 1, is_buying)
            # * If we can buy the stock.
            if is_buying:
                buy_val = (
                    maxProfitHelper(start_idx + 1, not is_buying) - prices[start_idx]
                )
                dp[(start_idx, is_buying)] = max(buy_val, cooldown_val)
            # * If we need to sell the stock to make profit.
            else:
                # * Move the start_idx to start_idx + 2 after we sell the stock as we need
                # * to cooldown before buying the new stock, i.e., skip the next element.
                sell_val = (
                    maxProfitHelper(start_idx + 2, not is_buying) + prices[start_idx]
                )
                dp[(start_idx, is_buying)] = max(sell_val, cooldown_val)

            return dp[(start_idx, is_buying)]

        return maxProfitHelper(0, True)


# @lc code=end
