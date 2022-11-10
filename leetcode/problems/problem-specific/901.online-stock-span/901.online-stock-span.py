#
# @lc app=leetcode id=901 lang=python3
#
# [901] Online Stock Span
#

# @lc code=start

# * Monotonic Decreasing Stack Solution | O(1) Time | O(n) Space
# * n -> The number of calls to next func


class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        res = 1
        while self.stack and price >= self.stack[-1][0]:
            res += self.stack.pop()[1]

        self.stack.append((price, res))

        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end
