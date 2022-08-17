#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start

# * Two Pointers Solution | O(n) Time | O(1) Space
# * n -> The length of height array

class Solution:
    def trap(self, height: List[int]) -> int:
        height_length = len(height)
        left, right = 0, height_length-1
        left_max, right_max = 0, 0
        result = 0
        while left < right:
            cur_left_val, cur_right_val = height[left], height[right]
            # * Left Half
            if cur_left_val <= cur_right_val:
                if cur_left_val >= left_max:
                    left_max = cur_left_val
                else:
                    result += left_max - cur_left_val

                left += 1

            # * Right Half
            else:
                if cur_right_val >= right_max:
                    right_max = cur_right_val
                else:
                    result += right_max - cur_right_val

                right -= 1

        return result

# @lc code=end
