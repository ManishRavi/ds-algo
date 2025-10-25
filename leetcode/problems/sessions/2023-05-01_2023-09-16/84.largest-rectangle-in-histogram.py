#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start

# * Iterative Stack Solution | O(n) Time | O(n) Space
# * n -> The length of heights array


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights_stack = []
        max_area = 0
        for idx, height in enumerate(heights):
            start_idx = idx
            while heights_stack and height <= heights_stack[-1][1]:
                stack_idx, stack_height = heights_stack.pop()
                max_area = max(max_area, stack_height * (idx - stack_idx))
                start_idx = stack_idx
            heights_stack.append((start_idx, height))

        for idx, height in heights_stack:
            max_area = max(max_area, height * (len(heights) - idx))

        return max_area


# @lc code=end
