#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#

# @lc code=start

# * Iterative BFS Level Order Traversal Solution | O(n) Time | O(n) Space
# * n -> The number of nodes in the tree

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        if not root:
            return result

        # * BFS Traversal
        queue = collections.deque([root])
        while queue:
            level_order_values = []
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                level_order_values.append(cur_node.val)
                for children in cur_node.children:
                    queue.append(children)

            result.append(level_order_values)

        return result

# @lc code=end
