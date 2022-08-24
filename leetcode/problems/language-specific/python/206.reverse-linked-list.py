#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start

# * Iterative Dummy Head Solution | O(n) Time | O(1) Space
# * n -> The number of nodes in the linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy_head, cur = ListNode(), head
        while cur:
            next = cur.next
            cur.next = dummy_head.next
            dummy_head.next = cur
            cur = next

        return dummy_head.next

# @lc code=end
