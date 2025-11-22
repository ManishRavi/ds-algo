#
# @lc app=leetcode id=1498 lang=python3
#
# [1498] Number of Subsequences That Satisfy the Given Sum Condition
#

# @lc code=start

# * Two Pointers and 1-DP Solution | O(nlogn) Time | O(n) Space
# * n -> The length of nums array


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        res, MOD = 0, 10**9 + 7
        dp = [1]
        for _ in range(len(nums)):
            dp.append(dp[-1] << 1 % MOD)

        nums.sort()
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] + nums[right] <= target:
                res = (res + dp[right - left]) % MOD
                left += 1
            else:
                right -= 1

        return res


# @lc code=end
