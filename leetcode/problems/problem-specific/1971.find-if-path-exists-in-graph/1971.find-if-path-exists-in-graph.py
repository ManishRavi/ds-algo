#
# @lc app=leetcode id=1971 lang=python3
#
# [1971] Find if Path Exists in Graph
#

# @lc code=start

# * Recursive DFS Solution | O(v+e) Time | O(v+e) Space
# * v -> The number of vertices in the graph | e -> The number of edges in the graph


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        # * Stores src to dest mapping.
        # * Key -> src | Value -> [dest]
        graph = {i: [] for i in range(n)}
        # * To keep track of visiting nodes in the current DFS path.
        visited_set = set()

        def build_graph():
            for src, dest in edges:
                graph[src].append(dest)
                graph[dest].append(src)

        def validPathHelper(src):
            if src in visited_set:
                return False
            if src == destination:
                return True

            visited_set.add(src)
            for neighbor in graph[src]:
                if validPathHelper(neighbor):
                    return True

            return False

        build_graph()
        return validPathHelper(source)


# @lc code=end
