#
# @lc app=leetcode id=814 lang=python3
#
# [814] Binary Tree Pruning
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
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def pruneHelper(root):
            if not root:
                return True

            can_remove_left_node = pruneHelper(root.left)
            can_remove_right_node = pruneHelper(root.right)
            if can_remove_left_node:
                root.left = None
            if can_remove_right_node:
                root.right = None

            return can_remove_left_node and can_remove_right_node and root.val == 0

        # * Return None, if the root node's value is 0 and can be removed.
        return root if not pruneHelper(root) else None


# @lc code=end
