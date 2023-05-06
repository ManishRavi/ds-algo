#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start

# * Monotonic Decreasing Stack Solution | O(n) Time | O(n) Space
# * n -> The length of temperatures array


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temperatures_stack = []
        res = [0] * len(temperatures)
        for idx, temperature in enumerate(temperatures):
            while temperatures_stack and temperature > temperatures_stack[-1][1]:
                stack_idx, _ = temperatures_stack.pop()
                res[stack_idx] = idx - stack_idx
            temperatures_stack.append((idx, temperature))

        return res


# @lc code=end
