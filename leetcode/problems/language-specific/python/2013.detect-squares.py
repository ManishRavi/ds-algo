#
# @lc app=leetcode id=2013 lang=python3
#
# [2013] Detect Squares
#

# @lc code=start

# * Geometry Solution | O(n) Time | O(n) Space
# * n -> The number of add operations


class DetectSquares:
    def __init__(self):
        self.point_cnt_map = collections.defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.point_cnt_map[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        # * Convert the hashmap keys to a list to avoid RuntimeError as we might be adding
        # * a key to the hashmap (mutate) during the iteration if the key doesn't exist.
        for x, y in list(self.point_cnt_map):
            # * Find the diagonal point to the given input query point, i.e., The width
            # * and the height of the diagonal point and the query point will be equal.
            # * Also, all the points shouldn't lie in the same coordinate.
            if (abs(x - px) == abs(y - py)) and x != px and y != py:
                # * Multiply with the number of occurrences of the
                # * repeated point for all the 3 coordinates.
                res += (
                    self.point_cnt_map[(x, y)]
                    * self.point_cnt_map[(x, py)]
                    * self.point_cnt_map[(px, y)]
                )

        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
# @lc code=end
