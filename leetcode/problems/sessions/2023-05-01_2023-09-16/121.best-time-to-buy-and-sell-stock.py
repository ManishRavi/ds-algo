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
        left = 0
        res = 0
        for right in range(1, len(prices)):
            if prices[right] > prices[left]:
                res = max(res, prices[right] - prices[left])
            else:
                left = right

        return res


# @lc code=end
