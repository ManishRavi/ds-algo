#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float("-inf")

        def dfs(root):
            nonlocal max_path_sum

            if not root:
                return 0

            left_node_path_sum = max(0, dfs(root.left))
            right_node_path_sum = max(0, dfs(root.right))
            max_path_sum = max(
                max_path_sum, root.val + left_node_path_sum + right_node_path_sum
            )
            return root.val + max(left_node_path_sum, right_node_path_sum)

        dfs(root)
        return max_path_sum


# @lc code=end
