#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start

# * Iterative Bottom-Up Solution | O(n) Time | O(1) Space
# * n -> The length of cost array


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])

        return min(cost[-1], cost[-2])


# @lc code=end
