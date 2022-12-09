#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start

# * Recursive DFS Solution | O(n) Time | O(n) Space
# * n -> The number of nodes in the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leafSimilarHelper(root, leaf_nodes):
            if not root:
                return

            if not root.left and not root.right:
                leaf_nodes.append(root.val)
            leafSimilarHelper(root.left, leaf_nodes)
            leafSimilarHelper(root.right, leaf_nodes)
            return leaf_nodes

        return leafSimilarHelper(root1, []) == leafSimilarHelper(root2, [])


# @lc code=end
