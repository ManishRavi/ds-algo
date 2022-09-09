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
        # * Stores a pair of the start index and the height.
        # * Pair -> (start_index, height)
        stack = []
        max_area = 0
        for idx, height in enumerate(heights):
            start_idx = idx
            while stack and height <= stack[-1][1]:
                stack_idx, stack_height = stack.pop()
                # * Area of rectangle = length * width
                max_area = max(max_area, stack_height * (idx - stack_idx))
                start_idx = stack_idx
            stack.append((start_idx, height))

        # * Process the leftover elements from the stack.
        for idx, height in stack:
            # * Area of rectangle = length * width
            max_area = max(max_area, height * (len(heights) - idx))

        return max_area


# @lc code=end
