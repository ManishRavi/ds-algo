#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start

# * Priority Queue (Min Heap) Solution | O(nlogk) Time | O(k) Space
# * n -> The length of nums array | k -> The given input


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapify(self.min_heap)
        self._pop_from_heap()

    def add(self, val: int) -> int:
        heappush(self.min_heap, val)
        self._pop_from_heap()
        return self.min_heap[0]

    def _pop_from_heap(self):
        while len(self.min_heap) > self.k:
            heappop(self.min_heap)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end
