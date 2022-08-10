#
# @lc app=leetcode id=823 lang=python3
#
# [823] Binary Trees With Factors
#

# @lc code=start

# * DP Solution | O(n^2) Time | O(n) Space
# * n -> Length of arr array

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        arr.sort()
        dp = [1] * len(arr)
        index_mappings = {num: i for i, num in enumerate(arr)}
        for i in range(len(arr)):
            for j in range(i):
                if arr[i] % arr[j] == 0 and arr[i] // arr[j] in index_mappings:
                    dp[i] += dp[j] * dp[index_mappings[arr[i] // arr[j]]]
                    dp[i] %= MOD

        return sum(dp) % MOD

# @lc code=end
