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
        # * Stores vertex/course to prerequisite courses mapping.
        # * Key -> course | Value -> [prerequisite_course]
        graph = {idx: [] for idx in range(numCourses)}
        # * To keep track of visiting courses in the current DFS path.
        visited_set = set()

        def build_graph():
            for src, dest in prerequisites:
                graph[src].append(dest)

        def canFinishHelper(course_idx):
            # * If the course is already visited in the current DFS path then
            # * it's a cycle and we can't finish this course.
            if course_idx in visited_set:
                return False
            # * If there are no neighbors/prerequisite courses for the
            # * current course then we can finish this course.
            if not graph[course_idx]:
                return True

            visited_set.add(course_idx)
            for prerequisite_course in graph[course_idx]:
                if not canFinishHelper(prerequisite_course):
                    return False

            visited_set.remove(course_idx)
            # * Once we've successfully visited/finished all the prerequisite courses then
            # * we can mark the current course as finished so that it's not visited again.
            graph[course_idx] = []
            return True

        build_graph()
        for idx in range(numCourses):
            if not canFinishHelper(idx):
                return False

        return True


# @lc code=end
