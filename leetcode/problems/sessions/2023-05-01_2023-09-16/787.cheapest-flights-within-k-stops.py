#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start

# * Bellman Ford Algorithm Solution | O(k*(v+e)) Time | O(v) Space
# * k -> The given input | v -> The number of vertices in the graph |
# * e -> The number of edges in the graph


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        for _ in range(k + 1):
            cur_prices = prices[:]
            for src, dest, price in flights:
                if prices[src] + price < cur_prices[dest]:
                    cur_prices[dest] = prices[src] + price
            if cur_prices == prices:
                break

            prices = cur_prices

        return prices[dst] if prices[dst] != float("inf") else -1


# @lc code=end
