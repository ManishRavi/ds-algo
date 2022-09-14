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
        # * Stores a pair of cost and node.
        # * Pair -> (cost, node)
        min_heap = [(0, 0)]
        # * Start Prims's algorithm.
        while len(visited_set) < points_len:
            cur_cost, cur_node = heapq.heappop(min_heap)
            if cur_node in visited_set:
                continue

            min_cost += cur_cost
            visited_set.add(cur_node)
            for next_node in range(points_len):
                if next_node not in visited_set:
                    x1, y1 = points[cur_node]
                    x2, y2 = points[next_node]
                    next_cost = self.get_manhattan_distance(x1, x2, y1, y2)
                    heapq.heappush(min_heap, (next_cost, next_node))

        return min_cost

    def get_manhattan_distance(self, x1, x2, y1, y2):
        return abs(x1 - x2) + abs(y1 - y2)


# @lc code=end
