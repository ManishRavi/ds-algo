#
# @lc app=leetcode id=987 lang=python3
#
# [987] Vertical Order Traversal of a Binary Tree
#

# @lc code=start

# * Recursive DFS Preorder Traversal Solution | O(nlogn) Time | O(n) Space
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
        # * Key -> column | Value -> [(row, value)]
        col_rows_map = collections.defaultdict(list)

        def verticalTraversalHelper(root, row, col):
            if not root:
                return

            col_rows_map[col].append((row, root.val))
            verticalTraversalHelper(root.left, row + 1, col - 1)
            verticalTraversalHelper(root.right, row + 1, col + 1)

        verticalTraversalHelper(root, 0, 0)
        return [
            [val for _, val in sorted(col_rows_map[col])]
            for col in sorted(col_rows_map)
        ]


# @lc code=end
