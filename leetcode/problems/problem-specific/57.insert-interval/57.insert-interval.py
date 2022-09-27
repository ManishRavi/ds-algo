#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start

# * Iterative Solution | O(n) Time | O(n) Space
# * n -> The length of intervals array


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        inserted_intervals = []
        for idx, interval in enumerate(intervals):
            # * No Overlap Case.

            # * Insert before the current interval.
            # * Add the newInterval to the inserted intervals and return the inserted
            # * intervals appended with the remaining intervals if the end of the
            # * newInterval is less than the start of the current interval.
            if newInterval[1] < interval[0]:
                inserted_intervals.append(newInterval)
                return inserted_intervals + intervals[idx:]
            # * Insert after the current interval.
            # * Add the current interval to the inserted intervals if the start of
            # * the newInterval is greater than the end of the current interval.
            elif newInterval[0] > interval[1]:
                inserted_intervals.append(interval)

            # * Overlap Case.
            else:
                newInterval = [
                    min(newInterval[0], interval[0]),
                    max(newInterval[1], interval[1]),
                ]

        inserted_intervals.append(newInterval)
        return inserted_intervals


# @lc code=end
