#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#

# @lc code=start

# * Recursive DFS Solution | O(v+e) Time | O(v+e) Space
# * v -> The number of vertices in the graph | e -> The number of edges in the graph


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []

        def allPathsSourceTargetHelper(node, path):
            path.append(node)
            if node == len(graph) - 1:
                res.append(path[:])
                return

            for neighbor in graph[node]:
                allPathsSourceTargetHelper(neighbor, path)
                path.pop()

        allPathsSourceTargetHelper(0, [])
        return res


# @lc code=end
