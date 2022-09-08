#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start

# * Priority Queue (Max Heap) Solution | O(nlogn) Time | O(n) Space
# * n -> The length of stones array


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            y, x = -heapq.heappop(max_heap), -heapq.heappop(max_heap)
            if x != y:
                heapq.heappush(max_heap, -(y - x))

        return -max_heap[0] if max_heap else 0


# @lc code=end
