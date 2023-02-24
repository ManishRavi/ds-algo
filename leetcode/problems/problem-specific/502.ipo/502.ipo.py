#
# @lc app=leetcode id=502 lang=python3
#
# [502] IPO
#

# @lc code=start

# * Two Priority Queues Solution | O(nlogn) Time | O(n) Space
# * n -> The length of profits/capital array


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        max_profit_heap = []
        min_capital_heap = [project for project in zip(capital, profits)]
        heapify(min_capital_heap)

        while k:
            while min_capital_heap and min_capital_heap[0][0] <= w:
                _, p = heappop(min_capital_heap)
                heappush(max_profit_heap, -p)
            if not max_profit_heap:
                break

            w += -heappop(max_profit_heap)
            k -= 1

        return w


# @lc code=end
