#
# @lc app=leetcode id=1519 lang=python3
#
# [1519] Number of Nodes in the Sub-Tree With the Same Label
#

# @lc code=start

# * Recursive DFS Solution | O(n) Time | O(n) Space
# * n -> The number of nodes in the tree


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = {i: [] for i in range(n)}
        res = [0] * n

        def build_graph():
            for src, dest in edges:
                graph[src].append(dest)
                graph[dest].append(src)

        def dfs(cur, par):
            counts = [0] * 26
            for child in graph[cur]:
                if child != par:
                    child_counts = dfs(child, cur)
                    for i in range(26):
                        counts[i] += child_counts[i]

            counts[ord(labels[cur]) - ord("a")] += 1
            res[cur] = counts[ord(labels[cur]) - ord("a")]
            return counts

        build_graph()
        dfs(0, -1)
        return res


# @lc code=end
