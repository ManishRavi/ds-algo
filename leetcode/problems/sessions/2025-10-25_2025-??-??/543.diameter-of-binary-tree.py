#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start

# * Recursive DFS Solution | O(n) Time | O(h) Space
# * n -> The number of nodes in the tree | h -> The height of the tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def helper(root):
            nonlocal diameter

            if not root:
                return 0

            left_node_depth = helper(root.left)
            right_node_depth = helper(root.right)
            diameter = max(diameter, left_node_depth + right_node_depth)
            return 1 + max(left_node_depth, right_node_depth)

        helper(root)
        return diameter


# @lc code=end
