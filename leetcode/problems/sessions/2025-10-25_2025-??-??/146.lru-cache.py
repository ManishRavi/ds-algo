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
    def __init__(self, key=0, value=0, prev=None, next=None) -> None:
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = defaultdict(Node)
        self._dummy_head, self._dummy_tail = Node(), Node()
        self._dummy_head.next, self._dummy_tail.prev = (
            self._dummy_tail,
            self._dummy_head,
        )

    def get(self, key: int) -> int:
        if key in self._cache:
            cur_node = self._cache[key]
            self._remove_from_list(cur_node)
            self._insert_into_head(cur_node)
            return cur_node.value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            cur_node = self._cache[key]
            cur_node.value = value
            self._remove_from_list(cur_node)
        else:
            self._cache[key] = Node(key, value)

        self._insert_into_head(self._cache[key])
        if len(self._cache) > self._capacity:
            lru_node = self._dummy_tail.prev
            self._remove_from_list(lru_node)
            del self._cache[lru_node.key]

    def _insert_into_head(self, node):
        next = self._dummy_head.next
        node.next, next.prev = next, node
        self._dummy_head.next, node.prev = node, self._dummy_head

    def _remove_from_list(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
