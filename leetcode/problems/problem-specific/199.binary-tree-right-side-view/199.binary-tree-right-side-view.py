#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        # * Start BFS traversal.
        queue = collections.deque([root])
        while queue:
            right_most_node = None
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                right_most_node = cur_node
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            if right_most_node:
                res.append(right_most_node.val)

        return res


# @lc code=end
