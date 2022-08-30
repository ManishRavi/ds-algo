#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (p and not q) or (q and not p) or (p.val != q.val):
            return False

        is_left_node_same = self.isSameTree(p.left, q.left)
        is_right_node_same = self.isSameTree(p.right, q.right)
        return is_left_node_same and is_right_node_same

# @lc code=end
