#
# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
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
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res = float("inf")
        prev_node = None

        def dfs(root):
            nonlocal res, prev_node

            if not root:
                return

            dfs(root.left)
            if prev_node:
                res = min(res, root.val - prev_node.val)
            prev_node = root
            dfs(root.right)

        dfs(root)
        return res


# @lc code=end/uploads/2021/02/05/bst1.jpg
