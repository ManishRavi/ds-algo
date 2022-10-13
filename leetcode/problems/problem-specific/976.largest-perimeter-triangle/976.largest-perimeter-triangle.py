#
# @lc app=leetcode id=976 lang=python3
#
# [976] Largest Perimeter Triangle
#

# @lc code=start

# * Sorting Solution | O(nlogn) Time | O(1) Space
# * n -> The length of nums array


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 3, -1, -1):
            # * To form a triangle of non-zero area -> a + b > c.
            if nums[i] + nums[i + 1] > nums[i + 2]:
                # * Perimeter of a triangle -> a + b + c.
                return nums[i] + nums[i + 1] + nums[i + 2]

        return 0


# @lc code=end
