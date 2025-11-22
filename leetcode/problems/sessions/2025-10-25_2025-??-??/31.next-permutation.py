#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start

# * Logical Solution | O(n) Time | O(1) Space
# * n -> The length of nums array


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = len(nums) - 2
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1

        if pivot >= 0:
            next_greater_pivot = len(nums) - 1
            while nums[pivot] >= nums[next_greater_pivot]:
                next_greater_pivot -= 1

            nums[pivot], nums[next_greater_pivot] = (
                nums[next_greater_pivot],
                nums[pivot],
            )

        nums[pivot + 1 :] = nums[pivot + 1 :][::-1]


# @lc code=end
