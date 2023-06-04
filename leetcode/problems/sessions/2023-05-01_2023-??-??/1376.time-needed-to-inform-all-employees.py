#
# @lc app=leetcode id=1376 lang=python3
#
# [1376] Time Needed to Inform All Employees
#


# @lc code=start

# * Iterative BFS Solution | O(v+e) Time | O(v+e) Space
# * v -> The number of vertices in the graph | e -> The number of edges in the graph


class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        graph = {i: [] for i in range(n)}

        def build_graph():
            for idx, employee in enumerate(manager):
                if employee != -1:
                    graph[employee].append(idx)

        build_graph()
        queue = deque([(0, headID)])
        res = 0
        while queue:
            for _ in range(len(queue)):
                cur_val, cur_node = queue.popleft()
                res = max(res, cur_val)
                for neighbor in graph[cur_node]:
                    queue.append((cur_val + informTime[cur_node], neighbor))

        return res


# @lc code=end
