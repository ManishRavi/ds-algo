#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
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
    def goodNodes(self, root: TreeNode) -> int:
        def goodNodesHelper(root, max_value):
            if not root:
                return 0

            result = 1 if root.val >= max_value else 0
            max_value = max(max_value, root.val)
            result += goodNodesHelper(root.left, max_value)
            result += goodNodesHelper(root.right, max_value)
            return result

        return goodNodesHelper(root, root.val)

# @lc code=end
