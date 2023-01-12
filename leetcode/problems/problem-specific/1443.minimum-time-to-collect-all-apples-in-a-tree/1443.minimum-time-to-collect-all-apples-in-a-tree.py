#
# @lc app=leetcode id=1443 lang=python3
#
# [1443] Minimum Time to Collect All Apples in a Tree
#

# @lc code=start

# * Recursive DFS Solution | O(n) Time | O(n) Space
# * n -> The number of nodes in the tree


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = {i: [] for i in range(n)}

        def build_graph():
            for src, dest in edges:
                graph[src].append(dest)
                graph[dest].append(src)

        def dfs(cur, par):
            cur_time = 0
            for child in graph[cur]:
                if child != par:
                    child_time = dfs(child, cur)
                    if child_time or hasApple[child]:
                        cur_time += 2 + child_time

            return cur_time

        build_graph()
        return dfs(0, -1)


# @lc code=end
