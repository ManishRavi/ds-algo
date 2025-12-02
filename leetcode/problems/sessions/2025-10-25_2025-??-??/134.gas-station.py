#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start

# * Greedy Solution | O(n) Time | O(1) Space
# * n -> The length of gas or cost array


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total_gas = start_idx = 0
        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            if total_gas < 0:
                total_gas = 0
                start_idx = i + 1

        return start_idx


# @lc code=end
