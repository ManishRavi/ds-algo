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
        preorder_idx, inorder_idx_val_map = 0, {}
        # * Build a hashmap to store value -> its index mappings.
        # * Key -> Value | Value -> Index
        for idx, val in enumerate(inorder):
            inorder_idx_val_map[val] = idx

        def buildTreeHelper(left, right):
            nonlocal preorder_idx

            # * If there are no elements to construct the tree.
            if left > right:
                return None

            # * Select the preorder_idx element as the root and increment it.
            root_val = preorder[preorder_idx]
            inorder_root_val_idx = inorder_idx_val_map[root_val]
            preorder_idx += 1

            # * Build left and right subtree
            # * excluding inorder_idx_val_map[root_val] element because it's the root.
            root = TreeNode(
                root_val,
                buildTreeHelper(left, inorder_root_val_idx - 1),
                buildTreeHelper(inorder_root_val_idx + 1, right),
            )

            return root

        return buildTreeHelper(0, len(inorder) - 1)


# @lc code=end
