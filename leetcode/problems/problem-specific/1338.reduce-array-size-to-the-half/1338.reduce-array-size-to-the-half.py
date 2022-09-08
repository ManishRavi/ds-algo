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
        arr_len = len(arr)
        arr_counter = collections.Counter(arr)
        max_heap = [-num for num in arr_counter.values()]
        heapq.heapify(max_heap)

        res = 0
        while arr_len > len(arr) // 2:
            arr_len -= -heapq.heappop(max_heap)
            res += 1

        return res


# @lc code=end
