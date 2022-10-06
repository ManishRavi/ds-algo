#
# @lc app=leetcode id=623 lang=python3
#
# [623] Add One Row to Tree
#

# @lc code=start

# * Iterative BFS Level Order Traversal Solution | O(n) Time | O(n) Space
# * n -> The number of nodes in the tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)

        # * Start BFS traversal.
        queue = collections.deque([root])
        depth -= 1
        while queue and depth > 1:
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)

            depth -= 1

        while queue:
            cur_node = queue.popleft()
            new_left_node = TreeNode(val, cur_node.left, None)
            new_right_node = TreeNode(val, None, cur_node.right)
            cur_node.left, cur_node.right = new_left_node, new_right_node

        return root


# @lc code=end
