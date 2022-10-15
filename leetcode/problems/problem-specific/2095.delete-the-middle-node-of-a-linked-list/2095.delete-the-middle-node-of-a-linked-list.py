#
# @lc app=leetcode id=2095 lang=python3
#
# [2095] Delete the Middle Node of a Linked List
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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # * Delete the middle node.
        slow.next = slow.next.next
        return head


# @lc code=end
