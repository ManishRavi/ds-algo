#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start

# * Priority Queue (Min Heap) Solution | O(nlogk) Time | O(n) Space
# * n -> The length of nums array | k -> The given input


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums
        heapify(min_heap)
        while len(min_heap) > k:
            heappop(min_heap)

        return min_heap[0]


# @lc code=end
