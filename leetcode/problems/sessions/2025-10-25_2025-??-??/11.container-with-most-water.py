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
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            # * Max area = height * width
            cur_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, cur_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# @lc code=end
