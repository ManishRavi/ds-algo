#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
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
            return 0

        if self.rank[node1_parent] > self.rank[node2_parent]:
            self.parent[node2_parent] = node1_parent
            self.rank[node1_parent] += self.rank[node2_parent]
        else:
            self.parent[node1_parent] = node2_parent
            self.rank[node2_parent] += self.rank[node1_parent]
        return 1


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ROWS, COLS = len(isConnected), len(isConnected[0])
        dsu = DSU(ROWS + 1)
        res = ROWS
        for row in range(ROWS):
            for col in range(COLS):
                if isConnected[row][col] == 1:
                    res -= dsu.union(row, col)

        return res


# @lc code=end
