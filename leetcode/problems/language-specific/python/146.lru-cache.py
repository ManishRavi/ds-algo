#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start

# * Hash Table and Doubly Linked List Solution | O(1) Time | O(n) Space
# * n -> The number of put operations

# Definition for a doubly linked list.
class Node:
    def __init__(self, key=0, value=0, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:
    # Initialize the LRU cache with positive size capacity.
    def __init__(self, capacity: int):
        self.capacity = capacity
        # * Stores a key-value pair where the value is a doubly linked list.
        self.cache = {}
        # * Dummy head and tail help us to easily manage LRU cache eviction.
        self.dummy_head = Node()
        self.dummy_tail = Node()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    # __insert_into_head inserts a given node into the head.
    # This is mainly used to insert the most recently used (MRU) key to the front of the list.
    def __insert_into_head(self, node):
        next = self.dummy_head.next
        node.next, next.prev = next, node
        self.dummy_head.next, node.prev = node, self.dummy_head

    # __remove_from_list removes a given node from the list.
    # This is mainly used to remove the least recently used (LRU) key from the list.
    def __remove_from_list(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    # get returns the value of the key if the key exists, otherwise return -1.
    def get(self, key: int) -> int:
        if key in self.cache:
            cur_node = self.cache[key]
            self.__remove_from_list(cur_node)
            self.__insert_into_head(cur_node)
            return cur_node.value

        return -1

    # put updates the value of the key if the key exists.
    # Otherwise, adds the key-value pair to the cache. If the number of keys
    # exceeds the capacity from this operation then evicts the least recently used key.
    def put(self, key: int, value: int) -> None:
        # * Updates the value of the key if the key exists and removes the node from the list
        # * so as to insert the node to the front of the list as it's the MRU key.
        if key in self.cache:
            cur_node = self.cache[key]
            cur_node.value = value
            self.__remove_from_list(cur_node)

        # * Adds the key-value pair to the cache.
        else:
            self.cache[key] = Node(key, value)

        # * Inserts the node to the front of the list as it's the MRU key.
        self.__insert_into_head(self.cache[key])
        # * Evicts the LRU key since the cache exceeds the given capacity.
        if len(self.cache) > self.capacity:
            lru_node = self.dummy_tail.prev
            self.__remove_from_list(lru_node)
            del self.cache[lru_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
