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

        inorder = []

        def serializeHelper(root):
            if not root:
                inorder.append(str(None))
                return

            inorder.append(str(root.val))
            serializeHelper(root.left)
            serializeHelper(root.right)

        serializeHelper(root)
        return ','.join(inorder)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def deserializeHelper(nodes):
            value = next(nodes)
            if value == str(None):
                return None

            root = TreeNode(
                value,
                deserializeHelper(nodes),
                deserializeHelper(nodes)
            )

            return root

        return deserializeHelper(iter(data.split(',')))


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
