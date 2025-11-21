#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#

# @lc code=start

# * Prim's Algorithm Solution | O(ElogE) Time | O(E) Space
# * E -> The number of edges in the graph


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points_len = len(points)
        graph = defaultdict(list)

        def build_graph():
            for src in range(points_len):
                point1 = points[src]
                for dest in range(src + 1, points_len):
                    point2 = points[dest]
                    cost = self._get_manhattan_distance(*point1, *point2)
                    graph[src].append((dest, cost))
                    graph[dest].append((src, cost))

        build_graph()
        min_cost = 0
        min_heap = [(0, 0)]
        visited_set = set()
        while min_heap and len(visited_set) < points_len:
            cur_cost, cur_src = heappop(min_heap)
            if cur_src in visited_set:
                continue

            min_cost += cur_cost
            visited_set.add(cur_src)
            for dest, dest_cost in graph[cur_src]:
                if dest not in visited_set:
                    heappush(min_heap, (dest_cost, dest))

        return min_cost

    def _get_manhattan_distance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)


# @lc code=end
