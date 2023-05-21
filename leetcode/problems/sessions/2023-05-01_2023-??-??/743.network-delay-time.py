#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start

# * Dijkstra's Algorithm Solution | O(elogv) Time | O(v^2) Space
# * v -> The number of vertices in the graph | e -> The number of edges in the graph


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}

        def build_graph():
            for src, dest, time in times:
                graph[src].append((dest, time))

        build_graph()
        min_time = 0
        visited_set = set()
        min_heap = [(0, k)]
        while min_heap and len(visited_set) < n:
            cur_time, cur_node = heapq.heappop(min_heap)
            if cur_node in visited_set:
                continue

            min_time = cur_time
            visited_set.add(cur_node)
            for neighbor_node, neighbor_time in graph[cur_node]:
                if neighbor_node not in visited_set:
                    heapq.heappush(min_heap, (cur_time + neighbor_time, neighbor_node))

        return min_time if len(visited_set) == n else -1


# @lc code=end
