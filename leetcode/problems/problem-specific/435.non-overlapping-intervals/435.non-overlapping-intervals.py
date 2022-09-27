#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start

# * Greedy and Sorting Solution | O(nlogn) Time | O(1) Space
# * n -> The length of intervals array


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # * Sort the intervals in ascending order based on the start value.
        intervals.sort(key=lambda interval: interval[0])
        min_intervals = 0
        prev_end = intervals[0][1]
        for start, end in intervals[1:]:
            # * No Overlap.
            if start >= prev_end:
                prev_end = end
            # * Overlap.
            else:
                min_intervals += 1
                prev_end = min(prev_end, end)

        return min_intervals


# @lc code=end
