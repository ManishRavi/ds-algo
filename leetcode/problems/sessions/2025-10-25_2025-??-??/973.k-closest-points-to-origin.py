#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start

# * Priority Queue (Max Heap) Solution | O(nlogk) Time | O(k) Space
# * n -> The length of points array | k -> The given input


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for idx, point in enumerate(points):
            distance = self._get_euclidean_distance(*point, 0, 0)
            heappush(max_heap, (-distance, idx))
            if len(max_heap) > k:
                heappop(max_heap)

        res = []
        while max_heap:
            _, idx = heappop(max_heap)
            res.append(points[idx])

        return res

    def _get_euclidean_distance(self, x1, y1, x2, y2):
        return sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))


# @lc code=end
