#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start

# * Divide and Conquer Solution | O(nlogk) Time | O(1) Space
# * k -> The number of linked lists | n -> The number of nodes in two lists while merging


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) <= 0:
            return None

        lists_len = len(lists)
        interval = 1
        while interval < lists_len:
            for i in range(0, lists_len - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2

        return lists[0]

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
