#
# @lc app=leetcode id=1035 lang=python3
#
# [1035] Uncrossed Lines
#

# @lc code=start

# * Iterative Bottom-Up Solution | O(mn) Time | O(mn) Space
# * m -> The length of nums1 array | n -> The length of nums2 array


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_len, nums2_len = len(nums1), len(nums2)
        dp = [[0] * (nums2_len + 1) for _ in range(nums1_len + 1)]
        for i in range(1, nums1_len + 1):
            for j in range(1, nums2_len + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[nums1_len][nums2_len]


# @lc code=end
