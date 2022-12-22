#
# @lc app=leetcode id=886 lang=python3
#
# [886] Possible Bipartition
#

# @lc code=start

# * Recursive DFS Solution | O(v+e) Time | O(v+e) Space
# * v -> The number of vertices in the graph | e -> The number of edges in the graph


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = {i: [] for i in range(1, n + 1)}
        colors = [-1] * (n + 1)

        def build_graph():
            for src, dest in dislikes:
                graph[src].append(dest)
                graph[dest].append(src)

        def possibleBipartitionHelper(node, node_color):
            colors[node] = node_color
            for neighbor in graph[node]:
                if colors[node] == colors[neighbor]:
                    return False
                if colors[neighbor] == -1:
                    if not possibleBipartitionHelper(neighbor, 1 - node_color):
                        return False

            return True

        build_graph()
        for i in range(1, n + 1):
            if colors[i] == -1:
                if not possibleBipartitionHelper(i, 0):
                    return False

        return True


# @lc code=end
