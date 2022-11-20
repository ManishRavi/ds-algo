#
# @lc app=leetcode id=979 lang=python3
#
# [979] Distribute Coins in Binary Tree
#

# @lc code=start

# * Recursive DFS and Math Solution | O(n) Time | O(h) Space
# * n -> The number of nodes in the tree | h -> The height of the tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        min_moves = 0

        def distributeCoinsHelper(root):
            nonlocal min_moves

            if not root:
                return 0

            left_node_coins = distributeCoinsHelper(root.left)
            right_node_coins = distributeCoinsHelper(root.right)
            min_moves += abs(left_node_coins) + abs(right_node_coins)
            return root.val + left_node_coins + right_node_coins - 1

        distributeCoinsHelper(root)
        return min_moves


# @lc code=end
