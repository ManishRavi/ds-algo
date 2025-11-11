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
        self.small_max_heap, self.large_min_heap = [], []

    def addNum(self, num: int) -> None:
        heappush(self.small_max_heap, -num)
        if (
            self.small_max_heap
            and self.large_min_heap
            and -self.small_max_heap[0] > self.large_min_heap[0]
        ):
            heappush(self.large_min_heap, -heappop(self.small_max_heap))

        if len(self.small_max_heap) > len(self.large_min_heap) + 1:
            heappush(self.large_min_heap, -heappop(self.small_max_heap))
        if len(self.large_min_heap) > len(self.small_max_heap) + 1:
            heappush(self.small_max_heap, -heappop(self.large_min_heap))

    def findMedian(self) -> float:
        if len(self.small_max_heap) > len(self.large_min_heap):
            return -self.small_max_heap[0]
        elif len(self.large_min_heap) > len(self.small_max_heap):
            return self.large_min_heap[0]

        return (-self.small_max_heap[0] + self.large_min_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
