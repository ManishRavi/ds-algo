#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start

# * Binary Search Solution | O(logn) Time | O(1) Space
# * n -> The length of nums array


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums) - 1
        while left <= right:
            # * If the array is already sorted from left to right.
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            mid = left + (right - left) // 2
            res = min(res, nums[mid])
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return res


# @lc code=end
