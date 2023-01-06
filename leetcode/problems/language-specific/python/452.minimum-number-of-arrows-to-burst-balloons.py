#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start

# * Sorting and Greedy Solution | O(nlogn) Time | O(n) Space
# * n -> The length of points array


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: point[1])
        min_arrows = 0
        max_end_point = float("-inf")

        for start, end in points:
            if max_end_point < start:
                min_arrows += 1
                max_end_point = end

        return min_arrows


# @lc code=end
