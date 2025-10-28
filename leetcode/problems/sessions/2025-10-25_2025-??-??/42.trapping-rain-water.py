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
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        res = 0
        while left < right:
            cur_left_val, cur_right_val = height[left], height[right]
            if cur_left_val <= cur_right_val:
                if cur_left_val >= left_max:
                    left_max = cur_left_val
                else:
                    res += left_max - cur_left_val
                left += 1
            else:
                if cur_right_val >= right_max:
                    right_max = cur_right_val
                else:
                    res += right_max - cur_right_val
                right -= 1

        return res


# @lc code=end
