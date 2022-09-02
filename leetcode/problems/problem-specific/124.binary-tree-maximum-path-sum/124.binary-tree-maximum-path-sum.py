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
        max_path_sum = root.val

        def maxPathSumHelper(root):
            """ 
            Returns max path sum w\ split, i.e., Returns either root to left or root to right path sum.
            """

            nonlocal max_path_sum

            if not root:
                return 0

            # * To handle negative values compare them with 0 to get the max value.
            # * Don't consider them as they don't add up to the max path sum value.
            left_node_path_sum = max(maxPathSumHelper(root.left), 0)
            rigth_node_path_sum = max(maxPathSumHelper(root.right), 0)

            # * Compute max path sum w/ split (Include both left and right nodes path sum).
            max_path_sum = max(
                max_path_sum,
                root.val + left_node_path_sum + rigth_node_path_sum
            )

            return root.val + max(left_node_path_sum, rigth_node_path_sum)

        maxPathSumHelper(root)
        return max_path_sum

# @lc code=end
