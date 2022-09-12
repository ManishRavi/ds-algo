#
# @lc app=leetcode id=1383 lang=python3
#
# [1383] Maximum Performance of a Team
#

# @lc code=start

# * Sorting and Priority Queue (Min Heap) Solution | O(nlogn) Time | O(k) Space
# * n -> The given input


class Solution:
    def maxPerformance(
        self, n: int, speed: List[int], efficiency: List[int], k: int
    ) -> int:
        engineers = [engineer for engineer in zip(efficiency, speed)]
        # * Sort in descending order based on the efficiency.
        engineers.sort(key=lambda engineer: -engineer[0])
        min_heap = []
        max_performance = total_speed = 0
        for cur_efficiency, cur_speed in engineers:
            if len(min_heap) == k:
                total_speed -= heapq.heappop(min_heap)
            total_speed += cur_speed
            heapq.heappush(min_heap, cur_speed)
            max_performance = max(max_performance, cur_efficiency * total_speed)

        return max_performance % (10**9 + 7)


# @lc code=end
