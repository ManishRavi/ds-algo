#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start

# * Hash Table and Priority Queue (Max Heap) Solution | O(n) Time | O(n) Space
# * n -> The length of s string


class Solution:
    def frequencySort(self, s: str) -> str:
        s_counter = collections.Counter(s)
        max_heap = [(-count, char) for char, count in s_counter.items()]
        heapq.heapify(max_heap)
        res = []
        while max_heap:
            count, char = heapq.heappop(max_heap)
            count = -count
            res.extend([char] * count)

        return "".join(res)


# @lc code=end
