#
# @lc app=leetcode id=871 lang=python3
#
# [871] Minimum Number of Refueling Stops
#

# @lc code=start

# * Priority Queue (Max Heap) Solution | O(nlogn) Time | O(n) Space
# * n -> The length of stations array

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations_length, max_distance = len(stations), startFuel
        max_heap = []
        refill = 0
        i = 0
        while max_distance < target:
            while i < stations_length and max_distance >= stations[i][0]:
                heapq.heappush(max_heap, -stations[i][1])
                i += 1

            if not max_heap:
                return -1

            max_distance += -1 * heapq.heappop(max_heap)
            refill += 1

        return refill

# @lc code=end
