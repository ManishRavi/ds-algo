#
# @lc app=leetcode id=1578 lang=python3
#
# [1578] Minimum Time to Make Rope Colorful
#

# @lc code=start

# * Iterative Solution | O(n) Time | O(1) Space
# * n -> The length of colors string


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        min_time = 0
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                min_time += min(neededTime[i], neededTime[i - 1])
                # * Maximum value is being picked up because the element with the
                # * minimum value is used but the maximum value is still kept.
                neededTime[i] = max(neededTime[i], neededTime[i - 1])

        return min_time


# @lc code=end
