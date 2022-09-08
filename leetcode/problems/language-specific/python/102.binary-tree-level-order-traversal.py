#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start

# * Iterative BFS Solution | O(n) Time | O(n) Space
# * n -> The number of nodes in the tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        # * Start BFS traversal.
        queue = collections.deque([root])
        while queue:
            level_order_values = []
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                level_order_values.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            res.append(level_order_values)

        return res


# @lc code=end
