#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start

# * Fast & Slow Pointer Solution | O(n) Time | O(1) Space
# * n -> The number of nodes in the linked list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        first, second = head, prev
        while second and second.next:
            next1, next2 = first.next, second.next
            first.next = second
            second.next = next1
            first, second = next1, next2


# @lc code=end
