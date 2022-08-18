#
# @lc app=leetcode id=1338 lang=python3
#
# [1338] Reduce Array Size to The Half
#

# @lc code=start

# * Hash Table and Priority Queue (Max Heap) Solution | O(nlogn) Time | O(n) Space
# * n -> The length of arr array

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr_length = len(arr)
        arr_counter = collections.Counter(arr)
        max_heap = []
        for num in arr_counter.values():
            heapq.heappush(max_heap, -num)

        result = 0
        while arr_length > len(arr)//2:
            arr_length -= -1 * heapq.heappop(max_heap)
            result += 1

        return result

# @lc code=end
