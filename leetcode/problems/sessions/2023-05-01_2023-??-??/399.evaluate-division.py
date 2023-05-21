#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start

# * Iterative BFS Solution | O(n*(v+e)) Time | O(v+e) Space
# * v -> The number of vertices in the graph | e -> The number of edges in the graph |
# * n -> The length of queries array


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(list)

        def build_graph():
            for i, equation in enumerate(equations):
                src, dest = equation
                graph[src].append((dest, values[i]))
                graph[dest].append((src, 1 / values[i]))

        def bfs(src, dest):
            if src not in graph or dest not in graph:
                return -1

            queue = deque([(src, 1)])
            visited_set = set([src])
            while queue:
                cur_node, cur_val = queue.popleft()
                if cur_node == dest:
                    return cur_val

                for neighbor, neighbor_val in graph[cur_node]:
                    if neighbor not in visited_set:
                        queue.append((neighbor, cur_val * neighbor_val))
                        visited_set.add(neighbor)
            return -1

        build_graph()
        return [bfs(src, dest) for src, dest in queries]


# @lc code=end
