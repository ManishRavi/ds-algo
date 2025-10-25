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
            if newInterval[1] < interval[0]:
                inserted_intervals.append(newInterval)
                return inserted_intervals + intervals[idx:]
            elif newInterval[0] > interval[1]:
                inserted_intervals.append(interval)
            else:
                newInterval = [
                    min(newInterval[0], interval[0]),
                    max(newInterval[1], interval[1]),
                ]

        inserted_intervals.append(newInterval)
        return inserted_intervals


# @lc code=end
