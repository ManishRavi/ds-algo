#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start

# * Hash Table and Doubly Linked List Solution | O(1) Time | O(n) Space
# * n -> The given input capacity


# Definition for a doubly linked list.
class Node:
    def __init__(self, key=0, val=0, prev=None, next=None) -> None:
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = defaultdict(Node)
        self.dummy_head = Node()
        self.dummy_tail = Node()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def get(self, key: int) -> int:
        if key in self.cache:
            cur_node = self.cache[key]
            self._remove_from_list(cur_node)
            self._insert_into_head(cur_node)
            return cur_node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            cur_node = self.cache[key]
            cur_node.val = value
            self._remove_from_list(cur_node)
        else:
            self.cache[key] = Node(key, value)

        self._insert_into_head(self.cache[key])
        if len(self.cache) > self.capacity:
            lru_node = self.dummy_tail.prev
            self._remove_from_list(lru_node)
            del self.cache[lru_node.key]

    def _insert_into_head(self, node):
        next = self.dummy_head.next
        node.next, next.prev = next, node
        self.dummy_head.next, node.prev = node, self.dummy_head

    def _remove_from_list(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
