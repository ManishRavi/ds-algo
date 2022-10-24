#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# @lc code=start

# * Cyclic Sort Solution | O(n) Time | O(1) Space
# * n -> The length of nums array


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # * Start Cyclic Sort.
        i = 0
        while i < len(nums):
            # * Swap the elements if it isn't present at their required index.
            correct_idx = nums[i] - 1
            if nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1

        # * Find the duplicate & missing number.
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return [nums[i], i + 1]


# @lc code=end
