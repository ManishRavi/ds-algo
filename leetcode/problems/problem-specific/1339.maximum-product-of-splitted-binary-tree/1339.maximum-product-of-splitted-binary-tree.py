#
# @lc app=leetcode id=1339 lang=python3
#
# [1339] Maximum Product of Splitted Binary Tree
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
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        max_product = total_tree_sum = 0

        def maxProductHelper(root):
            nonlocal max_product

            if not root:
                return 0

            left_sum = maxProductHelper(root.left)
            right_sum = maxProductHelper(root.right)
            cur_subtree_sum = root.val + left_sum + right_sum
            max_product = max(
                max_product, (total_tree_sum - cur_subtree_sum) * cur_subtree_sum
            )
            return cur_subtree_sum

        total_tree_sum = maxProductHelper(root)
        maxProductHelper(root)
        return max_product % (10**9 + 7)


# @lc code=end
