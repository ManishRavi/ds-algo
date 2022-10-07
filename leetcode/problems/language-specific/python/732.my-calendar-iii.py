#
# @lc app=leetcode id=732 lang=python3
#
# [732] My Calendar III
#

# @lc code=start

# * Sweep-line Algorithm Solution | O(n^2) Time | O(n) Space
# * n -> The number of book operations


import sortedcontainers


class MyCalendarThree:
    def __init__(self):
        self.event_cnt_map = sortedcontainers.SortedDict()

    def book(self, start: int, end: int) -> int:
        self.event_cnt_map[start] = self.event_cnt_map.get(start, 0) + 1
        self.event_cnt_map[end] = self.event_cnt_map.get(end, 0) - 1
        max_count = cur_count = 0
        for val in self.event_cnt_map.values():
            cur_count += val
            max_count = max(max_count, cur_count)

        return max_count


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
# @lc code=end
