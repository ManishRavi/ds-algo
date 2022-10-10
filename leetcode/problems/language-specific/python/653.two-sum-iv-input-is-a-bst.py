#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
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
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums_set = set()

        def findTargetHelper(root):
            if not root:
                return False
            if (k - root.val) in nums_set:
                return True

            nums_set.add(root.val)
            return findTargetHelper(root.left) or findTargetHelper(root.right)

        return findTargetHelper(root)


# @lc code=end
