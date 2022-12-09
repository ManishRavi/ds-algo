#
# @lc app=leetcode id=1026 lang=python3
#
# [1026] Maximum Difference Between Node and Ancestor
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
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_ancestor_diff = 0

        def maxAncestorDiffHelper(root, prev_max, prev_min):
            nonlocal max_ancestor_diff

            if not root:
                return

            cur_max = max(prev_max, root.val)
            cur_min = min(prev_min, root.val)
            max_ancestor_diff = max(max_ancestor_diff, abs(cur_max - cur_min))
            maxAncestorDiffHelper(root.left, cur_max, cur_min)
            maxAncestorDiffHelper(root.right, cur_max, cur_min)

        maxAncestorDiffHelper(root, root.val, root.val)
        return max_ancestor_diff


# @lc code=end
