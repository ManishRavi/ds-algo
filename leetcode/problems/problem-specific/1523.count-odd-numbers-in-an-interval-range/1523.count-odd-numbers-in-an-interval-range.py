#
# @lc app=leetcode id=1523 lang=python3
#
# [1523] Count Odd Numbers in an Interval Range
#

# @lc code=start

# * Math Solution | O(1) Time | O(1) Space


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odd_count = (high - low) // 2
        if low % 2 or high % 2:
            odd_count += 1

        return odd_count


# @lc code=end
