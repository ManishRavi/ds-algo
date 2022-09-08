#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy_head = ListNode(0, head)
        prev_group = dummy_head
        while True:
            kth_node = self.get_kth_node(prev_group, k)
            if not kth_node:
                break

            # * Reverse the linked list in the current group.
            next_group = kth_node.next
            prev, cur = next_group, prev_group.next
            while cur != next_group:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next

            # * Modify the prev_group link.
            next = prev_group.next
            prev_group.next = kth_node
            prev_group = next

        return dummy_head.next

    def get_kth_node(self, head: Optional[ListNode], k: int):
        while head and k > 0:
            head = head.next
            k -= 1

        return head


# @lc code=end
