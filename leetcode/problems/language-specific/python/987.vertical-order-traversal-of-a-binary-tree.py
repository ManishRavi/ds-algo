#
# @lc app=leetcode id=987 lang=python3
#
# [987] Vertical Order Traversal of a Binary Tree
#

# @lc code=start

# * Recursive DFS Solution | O(nlogn) Time | O(n) Space
# * n -> The number of nodes in the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # * Stores a key-value pair where key is a column and value is an array of row and node value.
        # * column -> [(row, value)]
        vertical_mappings = collections.defaultdict(list)

        def verticalTraversalHelper(root, row=0, col=0):
            if not root:
                return

            vertical_mappings[col].append((row, root.val))
            verticalTraversalHelper(root.left, row + 1, col - 1)
            verticalTraversalHelper(root.right, row + 1, col + 1)

        verticalTraversalHelper(root)
        return [
            [value for _, value in sorted(vertical_mappings[key])]
            for key in sorted(vertical_mappings)
        ]

# @lc code=end
