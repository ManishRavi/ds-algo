#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start

# * Recursive DFS Inorder Traversal Solution | O(n) Time | O(h) Space
# * n -> The number of nodes in the tree | h -> The height of the tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        def inorderTraversalHelper(root):
            if not root:
                return

            inorderTraversalHelper(root.left)
            res.append(root.val)
            inorderTraversalHelper(root.right)

        inorderTraversalHelper(root)
        return res


# @lc code=end
