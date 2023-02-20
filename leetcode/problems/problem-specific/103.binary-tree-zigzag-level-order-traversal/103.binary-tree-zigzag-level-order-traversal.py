#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start

# * Iterative Two Stacks Level Order Traversal Solution | O(n) Time | O(n) Space
# * n -> The number of nodes in the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        left_to_right_stack = [root]
        right_to_left_stack = []
        while left_to_right_stack or right_to_left_stack:
            level_order_values = []
            for _ in range(len(left_to_right_stack)):
                cur_node = left_to_right_stack.pop()
                level_order_values.append(cur_node.val)
                if cur_node.left:
                    right_to_left_stack.append(cur_node.left)
                if cur_node.right:
                    right_to_left_stack.append(cur_node.right)
            if level_order_values:
                res.append(level_order_values[:])

            level_order_values = []
            for _ in range(len(right_to_left_stack)):
                cur_node = right_to_left_stack.pop()
                level_order_values.append(cur_node.val)
                if cur_node.right:
                    left_to_right_stack.append(cur_node.right)
                if cur_node.left:
                    left_to_right_stack.append(cur_node.left)
            if level_order_values:
                res.append(level_order_values[:])

        return res


# @lc code=end
