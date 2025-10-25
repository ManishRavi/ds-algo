#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

# @lc code=start

# * Disjoint Set Union Solution | O(v+e) Time | O(v+e) Space
# * v -> The number of vertices in the graph | e -> The number of edges in the graph


class DSU:
    def __init__(self, n=0) -> None:
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        node1_parent, node2_parent = self.find(node1), self.find(node2)
        if node1_parent == node2_parent:
            return False

        if self.rank[node1_parent] > self.rank[node2_parent]:
            self.parent[node2_parent] = node1_parent
            self.rank[node1_parent] += self.rank[node2_parent]
        else:
            self.parent[node1_parent] = node2_parent
            self.rank[node2_parent] += self.rank[node1_parent]
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges) + 1)
        for edge in edges:
            if not dsu.union(*edge):
                return edge


# @lc code=end
