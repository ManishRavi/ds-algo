#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start

# * Priority Queue (Min Heap) Solution | O(nlogk) Time | O(k) Space
# * n -> The length of nums array | k -> The given input


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.k = k
        self.min_heap = nums
        heapify(self.min_heap)
        self._pop_from_heap()
        return self.min_heap[0]

    def _pop_from_heap(self):
        while len(self.min_heap) > self.k:
            heappop(self.min_heap)


# @lc code=end
