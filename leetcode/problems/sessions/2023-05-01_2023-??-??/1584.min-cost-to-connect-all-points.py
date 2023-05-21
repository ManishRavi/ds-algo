#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#

# @lc code=start

# * Prim's Algorithm Solution | O((n^2)*logn) Time | O(n^2) Space
# * n -> The length of points array


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points_len = len(points)
        min_cost = 0
        visited_set = set()
        min_heap = [(0, 0)]
        while len(visited_set) < points_len:
            cur_cost, cur_node = heapq.heappop(min_heap)
            if cur_node in visited_set:
                continue

            min_cost += cur_cost
            visited_set.add(cur_node)
            for next_node in range(points_len):
                if next_node not in visited_set:
                    next_cost = self._get_manhattan_distance(
                        *points[cur_node], *points[next_node]
                    )
                    heapq.heappush(min_heap, (next_cost, next_node))

        return min_cost

    def _get_manhattan_distance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)


# @lc code=end
