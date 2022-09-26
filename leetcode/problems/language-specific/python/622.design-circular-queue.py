#
# @lc app=leetcode id=622 lang=python3
#
# [622] Design Circular Queue
#

# @lc code=start

# * Doubly Linked List Solution | O(1) Time | O(n) Space
# * n -> The given input size


class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyCircularQueue:
    def __init__(self, k: int):
        self.total_size = k
        self.cur_size = 0
        self.dummy_front = Node()
        self.dummy_rear = Node()
        self.dummy_front.next = self.dummy_rear
        self.dummy_rear.prev = self.dummy_front

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = Node(value)
        self.dummy_rear.prev.next, new_node.prev = new_node, self.dummy_rear.prev
        new_node.next, self.dummy_rear.prev = self.dummy_rear, new_node
        self.cur_size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.dummy_front.next = self.dummy_front.next.next
        self.dummy_front.next.prev = self.dummy_front
        self.cur_size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.dummy_front.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.dummy_rear.prev.val

    def isEmpty(self) -> bool:
        return self.cur_size == 0

    def isFull(self) -> bool:
        return self.cur_size == self.total_size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end
