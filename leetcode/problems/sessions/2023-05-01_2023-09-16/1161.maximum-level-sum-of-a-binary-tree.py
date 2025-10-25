#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#

# @lc code=start

# * Iterative BFS Level Order Traversal Solution | O(n) Time | O(n) Space
# * n -> The number of nodes in the tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        smallest_level = cur_level = 0
        max_level_order_sum = float("-inf")
        queue = deque([root])
        while queue:
            cur_level += 1
            cur_level_order_sum = 0
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                cur_level_order_sum += cur_node.val
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)

            if cur_level_order_sum > max_level_order_sum:
                max_level_order_sum = cur_level_order_sum
                smallest_level = cur_level

        return smallest_level


# @lc code=end
