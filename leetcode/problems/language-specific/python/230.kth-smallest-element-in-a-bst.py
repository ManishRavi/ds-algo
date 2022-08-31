#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start

# * Iterative Inorder Traversal Solution | O(n) Time | O(h) Space
# * n -> The number of nodes in the tree | h -> The height of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        while cur or stack:
            # * Move left until we've a valid node.
            while cur:
                stack.append(cur)
                cur = cur.left

            # * Pop the topmost element from the stack.
            cur = stack.pop()
            k -= 1
            if not k:
                return cur.val

            # * Move right.
            cur = cur.right

# @lc code=end
