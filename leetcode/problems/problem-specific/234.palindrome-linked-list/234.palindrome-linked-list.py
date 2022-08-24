#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start

# * Fast and Slow Pointer Solution | O(n) Time | O(1) Space
# * n -> The number of nodes in the linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # * Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # * Reverse the linked list from the middle to end
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        # * Compare the values from the start to middle with middle to end (reversed)
        while prev:
            if head.val != prev.val:
                return False

            head, prev = head.next, prev.next

        return True

# @lc code=end
