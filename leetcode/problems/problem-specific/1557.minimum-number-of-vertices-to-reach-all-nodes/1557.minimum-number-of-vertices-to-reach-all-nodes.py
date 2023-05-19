#
# @lc app=leetcode id=1557 lang=python3
#
# [1557] Minimum Number of Vertices to Reach All Nodes
#

# @lc code=start

# * Recursive DFS Solution | O(v+e) Time | O(v) Space
# * v -> The number of vertices in the graph | e -> The number of edges in the graph


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        for _, dest in edges:
            indegree[dest] += 1

        res = []
        for i in range(n):
            if indegree[i] == 0:
                res.append(i)

        return res


# @lc code=end
