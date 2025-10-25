#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start

# * Iterative BFS and Hash Table Solution | O(v+e) Time | O(v) Space
# * v -> The number of vertices in the graph | e -> The number of edges in the graph


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return node

        original_clone_map = defaultdict(Node)
        queue = deque([node])
        visited_set = set([node])
        while queue:
            cur_node = queue.popleft()
            if cur_node not in original_clone_map:
                original_clone_map[cur_node] = Node(cur_node.val)

            for neighbor in cur_node.neighbors:
                if neighbor not in original_clone_map:
                    original_clone_map[neighbor] = Node(neighbor.val)

                original_clone_map[cur_node].neighbors.append(
                    original_clone_map[neighbor]
                )

                if neighbor not in visited_set:
                    queue.append(neighbor)
                    visited_set.add(neighbor)

        return original_clone_map[node]


# @lc code=end
