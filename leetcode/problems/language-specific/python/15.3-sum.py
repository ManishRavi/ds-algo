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
        nums_len = len(nums)
        res = []
        if nums_len <= 2:
            return res

        nums.sort()
        for i in range(0, nums_len - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, nums_len - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    right -= 1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1
                elif cur_sum < 0:
                    left += 1
                else:
                    right -= 1

        return res


# @lc code=end
