#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total_sum = 0

        def rangeSumBSTHelper(root):
            nonlocal total_sum
            if not root:
                return

            if low <= root.val <= high:
                total_sum += root.val
            if low < root.val:
                rangeSumBSTHelper(root.left)
            if high > root.val:
                rangeSumBSTHelper(root.right)

        rangeSumBSTHelper(root)
        return total_sum


# @lc code=end
