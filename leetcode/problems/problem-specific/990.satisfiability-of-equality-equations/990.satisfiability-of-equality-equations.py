#
# @lc app=leetcode id=990 lang=python3
#
# [990] Satisfiability of Equality Equations
#

# @lc code=start

# * Disjoint Set Union Solution | O(v+e) Time | O(v+e) Space
# * v -> The number of vertices in the graph | e -> The number of edges in the graph


class DSU:
    def __init__(self, n=0):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2, condition):
        node1_parent, node2_parent = self.find(node1), self.find(node2)
        if condition == "!=":
            if node1_parent == node2_parent:
                return False

            return True

        if self.rank[node1_parent] > self.rank[node2_parent]:
            self.parent[node2_parent] = node1_parent
            self.rank[node1_parent] += self.rank[node2_parent]
        else:
            self.parent[node1_parent] = node2_parent
            self.rank[node2_parent] += self.rank[node1_parent]
        return True


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        dsu = DSU(26)
        # * Sort the equations so that the == ones come first.
        equations.sort(key=lambda eqn: "==" not in eqn)
        for eqn in equations:
            if not dsu.union(ord(eqn[0]) - ord("a"), ord(eqn[3]) - ord("a"), eqn[1:3]):
                return False

        return True


# @lc code=end
