#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start

# * Recursive DFS Solution | O(n^2) Time | O(h) Space
# * n -> The number of nodes in the tree | h -> The height of the tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def pathSumHelper(root, cur_path):
            if not root:
                return

            cur_path.append(root.val)
            if not root.left and not root.right and sum(cur_path) == targetSum:
                res.append(cur_path[:])

            pathSumHelper(root.left, cur_path)
            pathSumHelper(root.right, cur_path)
            cur_path.pop()

        pathSumHelper(root, [])
        return res


# @lc code=end
