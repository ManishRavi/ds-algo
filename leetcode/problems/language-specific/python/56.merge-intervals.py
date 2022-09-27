#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start

# * Sorting Solution | O(nlogn) Time | O(n) Space
# * n -> The length of intervals array


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # * Sort the intervals in ascending order based on the start value.
        intervals.sort(key=lambda interval: interval[0])
        merged_intervals = []
        for interval in intervals:
            # * Add the current interval to the merged intervals if the merged intervals is empty
            # * or if the current interval doesn't overlap with the previous merged interval.
            if not merged_intervals or merged_intervals[-1][1] < interval[0]:
                merged_intervals.append(interval)
            else:
                # * Else there is overlap, so we merge the current and previous intervals.
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])

        return merged_intervals


# @lc code=end
