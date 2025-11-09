#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_idx, inorder_val_idx_map = 0, {}
        for idx, val in enumerate(inorder):
            inorder_val_idx_map[val] = idx

        def helper(left, right):
            nonlocal preorder_idx

            if left > right:
                return None

            root_val = preorder[preorder_idx]
            inorder_root_val_idx = inorder_val_idx_map[root_val]
            preorder_idx += 1

            root = TreeNode(
                root_val,
                helper(left, inorder_root_val_idx - 1),
                helper(inorder_root_val_idx + 1, right),
            )
            return root

        return helper(0, len(inorder) - 1)


# @lc code=end
