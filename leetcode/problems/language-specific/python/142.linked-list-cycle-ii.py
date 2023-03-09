#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start

# * Floyd's Tortoise and Hare Cycle Detection Solution | O(n) Time | O(1) Space
# * n -> The number of nodes in the linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break
        else:
            return None

        slow2 = head
        while slow != slow2:
            slow, slow2 = slow.next, slow2.next

        return slow2


# @lc code=end
