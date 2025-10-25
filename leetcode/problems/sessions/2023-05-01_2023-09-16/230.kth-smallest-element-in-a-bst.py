#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start

# * Iterative DFS Solution | O(n) Time | O(n) Space
# * n -> The number of nodes in the tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur_node = root
        while stack or cur_node:
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left

            cur_node = stack.pop()
            k -= 1
            if k == 0:
                return cur_node.val

            cur_node = cur_node.right


# @lc code=end
