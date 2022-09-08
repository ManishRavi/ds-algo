#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start

# * Binary Search Solution | O(logn) Time | O(1) Space
# * n -> The length of nums array


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            # * If the left half is sorted.
            elif nums[left] <= nums[mid]:
                # * If the target lies on the left half.
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # * If the right half is sorted.
            else:
                # * If the target lies on the right half.
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


# @lc code=end
