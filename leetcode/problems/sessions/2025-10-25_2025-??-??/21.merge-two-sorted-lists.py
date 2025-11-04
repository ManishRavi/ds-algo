#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start

# * Iterative Dummy Head Solution | O(m+n) Time | O(1) Space
# * m -> The number of nodes in the linked list1 | n -> The number of nodes in the linked list2


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1

        dummy_head = ListNode()
        cur = dummy_head
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next

            cur = cur.next

        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2

        return dummy_head.next


# @lc code=end
