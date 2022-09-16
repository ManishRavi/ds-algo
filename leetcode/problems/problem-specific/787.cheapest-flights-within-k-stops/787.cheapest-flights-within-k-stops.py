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
        # * Start Bellman Ford Algorithm.
        # * Iterate for k + 1 times since at most we can have k stops in-between src and dest.
        for _ in range(k + 1):
            cur_prices = prices[:]
            # * Visit all the edges for each iteration.
            for src, dest, price in flights:
                if prices[src] + price < cur_prices[dest]:
                    cur_prices[dest] = prices[src] + price
            # * Break if we haven't made any change to the price edge, i.e.,
            # * we found the shortest path even before the k + 1 iterations.
            if cur_prices == prices:
                break

            prices = cur_prices

        return prices[dst] if prices[dst] != float("inf") else -1


# @lc code=end
