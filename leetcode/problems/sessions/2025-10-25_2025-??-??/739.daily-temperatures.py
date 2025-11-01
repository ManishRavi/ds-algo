#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start

# * Monotonic Decreasing Stack Solution | (n) Time | O(n) Space
# * n -> The length of temperatures array


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for idx, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                _, stack_idx = stack.pop()
                res[stack_idx] = idx - stack_idx

            stack.append((temperature, idx))

        return res


# @lc code=end
