#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start

# * Recursive DFS Preorder Traversal Solution | O(n) Time | O(h) Space
# * n -> The number of nodes in the tree | h -> The height of the tree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        preorder = []

        def helper(root):
            if not root:
                preorder.append(str(None))
                return
            preorder.append(str(root.val))
            helper(root.left)
            helper(root.right)

        helper(root)
        return ",".join(preorder)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def helper(nodes):
            cur_val = next(nodes)
            if cur_val == str(None):
                return None

            root = TreeNode(cur_val, helper(nodes), helper(nodes))
            return root

        return helper(iter(data.split(",")))


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
