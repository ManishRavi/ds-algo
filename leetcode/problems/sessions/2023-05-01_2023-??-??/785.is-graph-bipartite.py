#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start

# * Recursive DFS Solution | O(v+e) Time | O(v+e) Space
# * v -> The number of vertices in the graph | e -> The number of edges in the graph


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n

        def dfs(node, node_color):
            colors[node] = node_color
            for neighbor in graph[node]:
                if colors[neighbor] != -1:
                    if colors[neighbor] == node_color:
                        return False
                else:
                    if not dfs(neighbor, 1 - node_color):
                        return False
            return True

        for i in range(n):
            if colors[i] == -1:
                if not dfs(i, 0):
                    return False
        return True


# @lc code=end
