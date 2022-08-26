#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start

# * Two Pointers Solution | O(n^2) Time | O(1) Space
# * n -> The length of nums array

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_length = len(nums)
        result = []
        if nums_length <= 2:
            return result

        nums.sort()
        i = 0
        while i < nums_length-2:
            left, right = i+1, nums_length-1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left_val = nums[left]
                    while left < right and left_val == nums[left]:
                        left += 1

                    right_val = nums[right]
                    while right > left and right_val == nums[right]:
                        right -= 1

                elif cur_sum < 0:
                    left += 1
                else:
                    right -= 1

            i_val = nums[i]
            while i < nums_length-2 and i_val == nums[i]:
                i += 1

        return result

# @lc code=end
