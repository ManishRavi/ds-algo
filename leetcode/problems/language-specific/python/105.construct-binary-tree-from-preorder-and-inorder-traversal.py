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
        cur_preorder_index, inorder_index_mappings = 0, {}
        # * Build a hashmap to store value -> its index mappings.
        for idx, val in enumerate(inorder):
            inorder_index_mappings[val] = idx

        def buildTreeHelper(left, right):
            nonlocal cur_preorder_index

            # * If there are no elements to construct the tree.
            if left > right:
                return None

            # * Select the cur_preorder_index element as the root and increment it.
            root_value = preorder[cur_preorder_index]
            inorder_root_value_index = inorder_index_mappings[root_value]
            cur_preorder_index += 1

            # * Build left and right subtree
            # * excluding inorder_index_mappings[root_value] element because it's the root.
            root = TreeNode(
                root_value,
                buildTreeHelper(left, inorder_root_value_index - 1),
                buildTreeHelper(inorder_root_value_index + 1, right)
            )

            return root

        return buildTreeHelper(0, len(inorder) - 1)

# @lc code=end
