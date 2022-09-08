#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start

# * Two Pointers and Sliding Window Solution | O(n) Time | O(1) Space
# * n -> The length of prices array


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices_len = len(prices)
        max_profit = 0
        left = 0
        for right in range(1, prices_len):
            if prices[right] > prices[left]:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right

        return max_profit


# @lc code=end
