#
# @lc app=leetcode id=1473 lang=python3
#
# [1473] Paint House III
#

# @lc code=start

# * Dyanamic Programming Solution | O(mtnn) Time | O(tn) Space
# * m -> Total length of houses array | n -> Number of Colors | t -> Neighborhood Blocks

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp1, dp2 = {(0, 0): 0}, {}
        for i, a in enumerate(houses):
            for cj in (range(1, n + 1) if a == 0 else [a]):
                for ci, b in dp1:
                    b2 = b + (ci != cj)
                    if b2 > target:
                        continue

                    dp2[cj, b2] = min(dp2.get((cj, b2), float(
                        'inf')), dp1[ci, b] + (cost[i][cj - 1] if cj != a else 0))

            dp1, dp2 = dp2, {}
        return min([dp1[c, b] for c, b in dp1 if b == target] or [-1])

# @lc code=end
