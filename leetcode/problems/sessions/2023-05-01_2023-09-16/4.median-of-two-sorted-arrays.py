#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start

# * Binary Search Solution | O(log(min(m, n))) Time | O(1) Space
# * m -> The length of nums1 array | n -> The length of nums2 array


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # * Swap the array so as to apply the binary search on the smaller array (nums1).
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        nums1_len, nums2_len = len(nums1), len(nums2)
        total_len = nums1_len + nums2_len
        left, right = 0, nums1_len
        while left <= right:
            partition1 = left + (right - left) // 2
            # * total_len + 1 -> To handle both even and odd lengths.
            partition2 = ((total_len + 1) // 2) - partition1

            left1 = nums1[partition1 - 1] if partition1 > 0 else float("-inf")
            right1 = nums1[partition1] if partition1 < nums1_len else float("inf")
            left2 = nums2[partition2 - 1] if partition2 > 0 else float("-inf")
            right2 = nums2[partition2] if partition2 < nums2_len else float("inf")

            if left1 <= right2 and left2 <= right1:
                # * If even length.
                if not total_len % 2:
                    return (max(left1, left2) + min(right1, right2)) / 2

                # * If odd length.
                return max(left1, left2)
            elif left1 > right2:
                right = partition1 - 1
            else:
                left = partition1 + 1


# @lc code=end
