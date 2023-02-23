#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start

# * Binary Search Solution | O(nlogm) Time | O(1) Space
# * n -> The length of weights array | m -> The sum of weights array


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        res = right

        def can_ship(capacity):
            ships, cur_capacity = 1, capacity
            for weight in weights:
                if cur_capacity - weight < 0:
                    ships += 1
                    cur_capacity = capacity
                cur_capacity -= weight

            return ships <= days

        while left <= right:
            capacity = left + (right - left) // 2
            if can_ship(capacity):
                res = capacity
                right = capacity - 1
            else:
                left = capacity + 1

        return res


# @lc code=end
