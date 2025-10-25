#
# @lc app=leetcode id=1851 lang=python3
#
# [1851] Minimum Interval to Include Each Query
#

# @lc code=start

# * Sorting and Priority Queue (Min Heap) Solution | O(nlogn+qlogq) Time | O(n) Space
# * n -> The length of intervals array | q -> The length of queries array


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda interval: interval[0])
        res = {}
        min_heap = []
        i = 0
        for query in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= query:
                left, right = intervals[i]
                heapq.heappush(min_heap, (right - left + 1, right))
                i += 1

            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            res[query] = min_heap[0][0] if min_heap else -1

        return [res[query] for query in queries]


# @lc code=end
