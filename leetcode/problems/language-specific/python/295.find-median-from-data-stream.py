#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start

# * Two Priority Queues Solution | O(logn) Time | O(n) Space
# * n -> The number of addNum operations


class MedianFinder:
    def __init__(self):
        # * Stores all the elements <= to large_min_heap elements.
        self.small_max_heap = []
        # * Stores all the elements >= to small_max_heap elements.
        self.large_min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_max_heap, -num)
        # * All the elements in the small_max_heap should be <= large_min_heap.
        if (
            self.small_max_heap
            and self.large_min_heap
            and not -self.small_max_heap[0] <= self.large_min_heap[0]
        ):
            heapq.heappush(self.large_min_heap, -heapq.heappop(self.small_max_heap))

        # * Rebalance the heaps if the following condition fails
        # * |len(small_max_heap) - len(large_min_heap)| <= 1.
        if len(self.small_max_heap) > len(self.large_min_heap) + 1:
            heapq.heappush(self.large_min_heap, -heapq.heappop(self.small_max_heap))
        if len(self.large_min_heap) > len(self.small_max_heap) + 1:
            heapq.heappush(self.small_max_heap, -heapq.heappop(self.large_min_heap))

    def findMedian(self) -> float:
        # * If the heap lengths are odd.
        if len(self.small_max_heap) > len(self.large_min_heap):
            return -self.small_max_heap[0]
        if len(self.large_min_heap) > len(self.small_max_heap):
            return self.large_min_heap[0]

        # * If the heap lengths are even.
        return (-self.small_max_heap[0] + self.large_min_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
