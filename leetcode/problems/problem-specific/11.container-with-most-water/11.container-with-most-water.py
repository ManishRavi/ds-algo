#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start

# * Two Pointers Solution | O(n) Time | O(1) Space
# * n -> The length of height array


class Solution:
    def maxArea(self, height: List[int]) -> int:
        height_len = len(height)
        left, right = 0, height_len - 1
        max_amount_of_water = 0
        while left < right:
            # * Area of rectangle = length * width
            cur_area = min(height[left], height[right]) * (right - left)
            max_amount_of_water = max(max_amount_of_water, cur_area)
            # * Move the shorter height pointer.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_amount_of_water


# @lc code=end
