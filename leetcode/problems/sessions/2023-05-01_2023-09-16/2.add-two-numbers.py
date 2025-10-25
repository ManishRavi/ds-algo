#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start

# * Iterative Math and Dummy Head Solution | O(max(m, n)) Time | O(1) Space
# * m -> The number of nodes in the linked list l1 | n -> The number of nodes in the linked list l2


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy_head = ListNode()
        cur = dummy_head
        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            carry += l1_val + l2_val
            cur.next = ListNode(carry % 10)
            carry //= 10

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_head.next


# @lc code=end
