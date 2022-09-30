#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#

# @lc code=start

# * Sorting and Sorted List Solution | O(nlogn) Time | O(n) Space
# * n -> The length of buildings array


import sortedcontainers


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # * EC:1 -> If more than two points have the same start point, then we choose the
        # * point with the highest height first as it overshadows the lowest height.
        # * EC:2 -> If more than two points have the same end point, then we choose the
        # * point with the lowest height first as it undershadows the highest height.
        # * EC:3 -> If a point starts where another point ends, then we choose the
        # * start point first before we choose the end point.

        points = []
        # * Build the start and the end points of the
        # * x coordinate along with their heights.
        for start, end, height in buildings:
            # * Insert the x coordinate start point with height as negative
            # * value to handle all the 3 edge cases while sorting it.
            points.append((start, -height))
            points.append((end, height))

        # * This handles all the 3 edge cases as we're storing
        # * the start point heights as negative values.
        points.sort()
        # * Using SortedList instead of Priority Queue (Max Heap) to
        # * support the removal of a given element in O(logn) time.
        heights = sortedcontainers.SortedList([0])
        res = []

        for point in points:
            x, height = point
            # * If the height is less than 0 then it indicates the start point
            # * in which case we insert the height into the SortedList.
            if height < 0:
                heights.add(-height)
            # * Else it indicates the end point in which case
            # * we remove the height from the SortedList.
            else:
                heights.remove(height)

            # * Add the point to the result iff the max height has been changed.
            if not res or res[-1][1] != heights[-1]:
                res.append([x, heights[-1]])

        return res


# @lc code=end
