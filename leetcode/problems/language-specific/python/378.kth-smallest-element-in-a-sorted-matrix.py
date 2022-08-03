#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start

# * Priority Queue Solution | O(n^2) Time | O(k) Space
# * n -> Number of rows and columns

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        max_heap = []
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                heapq.heappush(max_heap, -matrix[row][col])
                if len(max_heap) > k:
                    heapq.heappop(max_heap)

        return -1*max_heap[0]
# @lc code=end
