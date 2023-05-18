#
# @lc app=leetcode id=2130 lang=python3
#
# [2130] Maximum Twin Sum of a Linked List
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
    def pairSum(self, head: Optional[ListNode]) -> int:
        # * 1. Find the middle of the linked list.
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        # * 2. Reverse the linked list from the middle.
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        # * 3. Find the max. twin sum.
        max_twin_sum = 0
        first, second = head, prev
        while second:
            max_twin_sum = max(max_twin_sum, first.val + second.val)
            first, second = first.next, second.next

        return max_twin_sum


# @lc code=end
