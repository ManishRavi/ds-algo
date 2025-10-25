#
# @lc app=leetcode id=2215 lang=python3
#
# [2215] Find the Difference of Two Arrays
#

# @lc code=start

# * Hash Table Solution | O(m+n) Time | O(m+n) Space
# * m -> The length of nums1 array | n -> The length of nums2 array


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set, nums2_set = set(nums1), set(nums2)
        return [nums1_set.difference(nums2_set), nums2_set.difference(nums1_set)]


# @lc code=end
