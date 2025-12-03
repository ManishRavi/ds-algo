#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start

# * Sorting Solution | O(nlogn) Time | O(1) Space
# * n -> The length of intervals array


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        min_intervals = 0
        prev_end = None
        for start, end in intervals:
            if prev_end is None or prev_end <= start:
                prev_end = end
            else:
                min_intervals += 1
                prev_end = min(prev_end, end)

        return min_intervals


# @lc code=end
