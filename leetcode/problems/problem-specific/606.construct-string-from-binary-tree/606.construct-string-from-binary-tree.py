#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
#

# @lc code=start

# * Recursive DFS Preorder Traversal Solution | O(n) Time | O(h) Space
# * n -> The number of nodes in the tree | h -> The height of the tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []

        def tree2strHelper(root):
            if not root:
                return

            res.append("(")
            res.append(str(root.val))
            if root.right and not root.left:
                res.append("()")
            tree2strHelper(root.left)
            tree2strHelper(root.right)
            res.append(")")

        tree2strHelper(root)
        return "".join(res[1:-1])


# @lc code=end
