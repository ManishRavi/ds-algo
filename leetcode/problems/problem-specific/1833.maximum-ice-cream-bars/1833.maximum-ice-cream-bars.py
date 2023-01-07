#
# @lc app=leetcode id=1833 lang=python3
#
# [1833] Maximum Ice Cream Bars
#

# @lc code=start

# * Priority Queue (Min Heap) and Greedy Solution | O(klogn) Time | O(1) Space
# * n -> The length of costs array | k -> The maximum number of ice cream bars


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        heapify(costs)
        max_ice_cream_bars = 0
        while costs:
            coins -= heappop(costs)
            if coins >= 0:
                max_ice_cream_bars += 1
            else:
                break

        return max_ice_cream_bars


# @lc code=end
