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
        graph = {course: [] for course in range(numCourses)}
        visited_set = set()
        res_set = set()
        res = []

        def build_graph():
            for src, dest in prerequisites:
                graph[src].append(dest)

        def helper(course):
            if course in visited_set:
                return False
            if course in res_set:
                return True

            visited_set.add(course)
            for prerequisite_course in graph[course]:
                if not helper(prerequisite_course):
                    return False

            visited_set.remove(course)
            res.append(course)
            res_set.add(course)
            return True

        build_graph()
        for course in range(numCourses):
            if not helper(course):
                return []

        return res


# @lc code=end
