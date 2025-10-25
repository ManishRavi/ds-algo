#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start

# * Priority Queue (Min Heap) Solution | O(klogn) Time | O(n) Space
# * n -> The length of points array | k -> The given input


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [
            (self._get_euclidean_distance(*point, *(0, 0)), idx)
            for idx, point in enumerate(points)
        ]

        heapify(min_heap)
        res = []
        while k > 0:
            res.append(points[heappop(min_heap)[1]])
            k -= 1

        return res

    def _get_euclidean_distance(self, x1, y1, x2, y2):
        return sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))


# @lc code=end
