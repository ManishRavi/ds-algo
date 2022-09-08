#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start

# * Two Pointers and Binary Search Solution | O(n) Time | O(1) Space
# * n -> The length of numbers array


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers_len = len(numbers)
        left, right = 0, numbers_len - 1
        while left < right:
            cur_sum = numbers[left] + numbers[right]
            if cur_sum == target:
                return [left + 1, right + 1]
            elif cur_sum < target:
                left += 1
            else:
                right -= 1


# @lc code=end
