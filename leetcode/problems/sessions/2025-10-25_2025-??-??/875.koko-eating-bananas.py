#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start


# * Binary Search Solution | O(n*log(max(p))) Time | O(1) Space
# * n -> The length of piles array | p -> The given input piles array


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        eating_speed = right
        while left <= right:
            mid = left + (right - left) // 2
            total_hours = 0
            for banana in piles:
                total_hours += math.ceil(banana / mid)

            if total_hours <= h:
                eating_speed = min(eating_speed, mid)
                right = mid - 1
            else:
                left = mid + 1

        return eating_speed


# @lc code=end
