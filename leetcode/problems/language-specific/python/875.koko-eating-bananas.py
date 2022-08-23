#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start

# * Binary Search Solution | O(m*log(max(p))) | O(1) Space
# * m -> The length of piles array | p -> Given piles array

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        k = right
        while left <= right:
            mid = left + (right - left) // 2
            total_hours = 0
            for bananas in piles:
                total_hours += math.ceil(bananas / mid)
            if total_hours <= h:
                k = min(k, mid)
                right = mid - 1
            else:
                left = mid + 1

        return k

# @lc code=end
