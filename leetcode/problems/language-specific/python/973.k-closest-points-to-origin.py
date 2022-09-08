#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start

# * Priority Queue (Min Heap) Solution | O(klogn) Time | O(n) Space
# * n -> The length of points array


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        # * Stores a pair of distance and index.
        # * Pair -> (distance, index)
        min_heap = []
        for idx, point in enumerate(points):
            x, y = point
            distance = self._get_euclidean_distance(x, 0, y, 0)
            min_heap.append((distance, idx))

        heapq.heapify(min_heap)
        while k > 0:
            _, heap_idx = heapq.heappop(min_heap)
            res.append(points[heap_idx])
            k -= 1

        return res

    def _get_euclidean_distance(self, x1, x2, y1, y2):
        # * sqrt is optional here since we're just finding out the closest points but not the distance.
        # * So, comparing the values without sqrt would also work.
        return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))


# @lc code=end
