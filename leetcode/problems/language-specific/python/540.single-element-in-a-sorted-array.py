#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#

# @lc code=start

# * Binary Search Solution | O(logn) Time | O(1) Space
# * n -> The length of nums array


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        nums_len = len(nums)
        left, right = 0, nums_len - 1
        while left <= right:
            mid = left + (right - left) // 2
            if (mid - 1 < 0 or nums[mid - 1] != nums[mid]) and (
                mid + 1 > nums_len - 1 or nums[mid] != nums[mid + 1]
            ):
                return nums[mid]

            left_size = mid - 1 if nums[mid - 1] == nums[mid] else mid
            if left_size % 2:
                right = mid - 1
            else:
                left = mid + 1


# @lc code=end
