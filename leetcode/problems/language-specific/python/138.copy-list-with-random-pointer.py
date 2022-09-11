#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start

# * Two Pass and Hash Table Solution | O(n) Time | O(n) Space
# * n -> The number of nodes in the linked list


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        original_clone_map = collections.defaultdict(lambda: None)
        # * 1st Pass -> Clone a node and store the mapping of the original to clone in a hashmap.
        cur = head
        while cur:
            original_clone_map[cur] = Node(cur.val)
            cur = cur.next

        # * 2nd Pass -> Populate the next and random pointers by leveraging a hashmap
        # * to get direct access to its clone node from the original node.
        cur = head
        while cur:
            clone_node = original_clone_map[cur]
            clone_node.next = original_clone_map[cur.next]
            clone_node.random = original_clone_map[cur.random]
            cur = cur.next

        return original_clone_map[head]


# @lc code=end
