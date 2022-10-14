#
# @lc app=leetcode id=237 lang=python3
#
# [237] Delete Node in a Linked List
#

# @lc code=start

# * Tricky Solution | O(1) Time | O(1) Space


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # * Set the current node value to the next node value.
        node.val = node.next.val
        # * Delete the next node.
        node.next = node.next.next


# @lc code=end
