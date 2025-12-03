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
        merged_intervals = []
        for idx, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                merged_intervals.append(newInterval)
                return merged_intervals + intervals[idx:]
            elif newInterval[0] > interval[1]:
                merged_intervals.append(interval)
            else:
                newInterval = [
                    min(newInterval[0], interval[0]),
                    max(newInterval[1], interval[1]),
                ]

        merged_intervals.append(newInterval)
        return merged_intervals


# @lc code=end
