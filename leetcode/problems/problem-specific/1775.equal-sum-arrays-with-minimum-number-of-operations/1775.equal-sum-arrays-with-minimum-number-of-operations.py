#
# @lc app=leetcode id=1775 lang=python3
#
# [1775] Equal Sum Arrays With Minimum Number of Operations
#

# @lc code=start

# * Greedy and Sorting Solution | O(nlogn) Time | O(n) Space
# * n -> The length of nums1 and nums2 array


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        total_sum1, total_sum2 = sum(nums1), sum(nums2)
        if total_sum1 == total_sum2:
            return 0

        # * Swap the array so as to increase the values in the smaller array (nums1)
        # * and decrease the values in the larger array (nums2).
        if total_sum2 < total_sum1:
            nums1, nums2 = nums2, nums1

        # * To increase the value -> UPPER_LIMIT (6) - num.
        # * To decrease the value -> num - LOWER_LIMIT (1).
        nums = [6 - num for num in nums1] + [num - 1 for num in nums2]
        nums.sort(reverse=True)
        sum_diff = abs(total_sum1 - total_sum2)
        count = 0
        for num in nums:
            count += 1
            sum_diff -= num
            if sum_diff <= 0:
                return count

        return -1


# @lc code=end
