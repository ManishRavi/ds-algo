#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start

# * Two Pointers and Dummy Head Solution | O(n) Time | O(1) Space
# * n -> The number of nodes in the linked list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        dummy_head = ListNode(0, head)
        left = dummy_head
        right = head
        # * Move the right pointer by n times.
        while n > 0:
            right = right.next
            n -= 1

        # * Move both the left and right pointers until right reaches the end of the list.
        # * After the loop, left will be pointing at the node just before the nth node.
        while right:
            left = left.next
            right = right.next

        # * Delete the node.
        left.next = left.next.next
        return dummy_head.next


# @lc code=end
