#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start

# * Recursive DFS Solution | O(mn) Time | O(h) Space
# * m -> The number of nodes in the root tree | n -> The number of nodes in the subRoot tree
# * h -> The height of the root tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        return (
            self.isSameTree(root, subRoot) or
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (p and not q) or (q and not p) or (p.val != q.val):
            return False

        is_left_node_same = self.isSameTree(p.left, q.left)
        is_right_node_same = self.isSameTree(p.right, q.right)
        return is_left_node_same and is_right_node_same

# @lc code=end
