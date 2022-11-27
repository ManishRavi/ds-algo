#
# @lc app=leetcode id=1235 lang=python3
#
# [1235] Maximum Profit in Job Scheduling
#

# @lc code=start

# * Iterative Bottom-Up Solution | O(nlogn) Time | O(n) Space
# * n -> The length of startTime array


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda job: job[1])
        profits, end_times = [0], [0]

        for s, e, p in jobs:
            profit_till_start_time = profits[bisect.bisect_left(end_times, s + 1) - 1]
            profits.append(max(profits[-1], profit_till_start_time + p))
            end_times.append(e)

        return profits[-1]


# @lc code=end
