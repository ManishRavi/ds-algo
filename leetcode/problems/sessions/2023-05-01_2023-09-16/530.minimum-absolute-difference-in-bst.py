#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#

# @lc code=start

# * Recursive DFS Solution | O(n) Time | O(n) Space
# * n -> The number of nodes in the tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        inorder = []
        res = float("inf")

        def inorder_traversal(root):
            nonlocal inorder

            if not root:
                return root

            inorder_traversal(root.left)
            inorder.append(root.val)
            inorder_traversal(root.right)

        inorder_traversal(root)
        for i in range(1, len(inorder)):
            res = min(res, inorder[i] - inorder[i - 1])

        return res


# @lc code=end
