#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start

# * Recursive DFS and Topological Sort Solution | O(v+e) Time | O(v+e) Space
# * v -> The number of vertices in the graph | e -> The number of edges in the graph


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {course: [] for course in range(numCourses)}
        visited_set = set()

        def build_graph():
            for src, dest in prerequisites:
                graph[src].append(dest)

        def helper(course):
            if course in visited_set:
                return False
            if not graph[course]:
                return True

            visited_set.add(course)
            for prerequisite_course in graph[course]:
                if not helper(prerequisite_course):
                    return False

            visited_set.remove(course)
            graph[course] = []
            return True

        build_graph()
        for course in range(numCourses):
            if not helper(course):
                return False

        return True


# @lc code=end
