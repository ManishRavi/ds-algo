#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start

# * Two Pointers Solution | O(n) Time | O(1) Space
# * n -> The length of nums array


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]

        return left + 1


# @lc code=end
