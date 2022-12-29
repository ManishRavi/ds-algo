#
# @lc app=leetcode id=1962 lang=python3
#
# [1962] Remove Stones to Minimize the Total
#

# @lc code=start

# * Priority Queue (Max Heap) Solution | O(klogn) Time | O(n) Space
# * n -> The length of piles array | k -> The given input


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = [-pile for pile in piles]
        heapq.heapify(max_heap)
        while k:
            cur_pile = -heapq.heappop(max_heap)
            cur_pile -= cur_pile // 2
            if cur_pile:
                heapq.heappush(max_heap, -cur_pile)
            k -= 1

        return -sum(max_heap)


# @lc code=end
