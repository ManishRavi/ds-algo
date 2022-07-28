#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start

# * Depth First Search Solution | O(n) Time | O(h) Space
# * n -> Number of nodes in a tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(root):
            if not root:
                return root

            left_tail = dfs(root.left)
            right_tail = dfs(root.right)
            if left_tail:
                left_tail.right = root.right
                root.right = root.left
                root.left = None

            return right_tail or left_tail or root

        dfs(root)

# @lc code=end
