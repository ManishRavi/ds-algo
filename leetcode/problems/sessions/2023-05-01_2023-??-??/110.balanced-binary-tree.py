#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return True, 0

            is_left_subtree_balanced, left_node_depth = dfs(root.left)
            is_right_subtree_balanced, right_node_depth = dfs(root.right)
            return (
                is_left_subtree_balanced
                and is_right_subtree_balanced
                and abs(left_node_depth - right_node_depth) <= 1,
                1 + max(left_node_depth, right_node_depth),
            )

        is_tree_balanced, _ = dfs(root)
        return is_tree_balanced


# @lc code=end
