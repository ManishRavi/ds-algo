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
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        """Initialize the LRU cache with positive size capacity."""
        self.capacity = capacity
        # * Stores a key-value pair where the key is the given key and value is a doubly linked list.
        self.cache = collections.defaultdict(Node)
        # * Dummy head and tail help us to easily manage LRU cache eviction.
        self.dummy_head = Node()
        self.dummy_tail = Node()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def get(self, key: int) -> int:
        """Returns the value of the key if the key exists, otherwise returns -1."""
        if key in self.cache:
            cur_node = self.cache[key]
            self._remove_from_list(cur_node)
            self._insert_into_head(cur_node)
            return cur_node.val

        return -1

    def put(self, key: int, value: int) -> None:
        """Updates the value of the key if the key exists.
        Otherwise, adds the key-value pair to the cache. If the number of keys
        exceeds the capacity from this operation then evicts the least recently used key.
        """
        # * Updates the value of the key if the key exists and removes the node from the list
        # * so as to insert the node to the front of the list as it's the MRU key.
        if key in self.cache:
            cur_node = self.cache[key]
            cur_node.val = value
            self._remove_from_list(cur_node)
        # * Adds the key-value pair to the cache.
        else:
            self.cache[key] = Node(key, value)

        # * Inserts the node to the front of the list as it's the MRU key.
        self._insert_into_head(self.cache[key])
        # * Evicts the LRU key if the cache exceeds the given capacity.
        if len(self.cache) > self.capacity:
            lru_node = self.dummy_tail.prev
            self._remove_from_list(lru_node)
            del self.cache[lru_node.key]

    def _insert_into_head(self, node):
        """Inserts a given node into the head.
        This is mainly used to insert the most recently used (MRU) key to the front of the list.
        """
        next = self.dummy_head.next
        node.next, next.prev = next, node
        self.dummy_head.next, node.prev = node, self.dummy_head

    def _remove_from_list(self, node):
        """Removes a given node from the list.
        This is mainly used to remove the least recently used (LRU) key from the list.
        """
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
