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
        graph = defaultdict(list)

        def build_graph():
            for src, dest, time in times:
                graph[src].append((dest, time))

        build_graph()
        min_time = 0
        min_heap = [(0, k)]
        visited_set = set()
        while min_heap and len(visited_set) < n:
            cur_time, cur_src = heappop(min_heap)
            if cur_src in visited_set:
                continue

            min_time = cur_time
            visited_set.add(cur_src)
            for dest, dest_time in graph[cur_src]:
                if dest not in visited_set:
                    heappush(min_heap, (cur_time + dest_time, dest))

        return min_time if len(visited_set) == n else -1


# @lc code=end
