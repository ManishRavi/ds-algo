#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start

# * Recursive DFS and Topological Sort Solution | O(v+e) Time | O(v+e) Space
# * v -> The number of vertices in the graph | e -> The number of edges in the graph


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        visited_set = set()
        res, res_set = [], set()

        def build_graph():
            for src, dest in prerequisites:
                graph[src].append(dest)

        def dfs(course_idx):
            if course_idx in visited_set:
                return False
            if course_idx in res_set:
                return True

            visited_set.add(course_idx)
            for prerequisite_course in graph[course_idx]:
                if not dfs(prerequisite_course):
                    return False

            visited_set.remove(course_idx)
            res.append(course_idx)
            res_set.add(course_idx)
            return True

        build_graph()
        for i in range(numCourses):
            if not dfs(i):
                return []

        return res


# @lc code=end
