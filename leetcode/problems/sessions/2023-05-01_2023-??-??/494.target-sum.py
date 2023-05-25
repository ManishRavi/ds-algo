#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#


# @lc code=start

# * Recursive Top-Down Solution | O(n*(sum(nums))) Time | O(n*(sum(nums))) Space
# * n -> The length of nums array


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memcache = {}

        def dfs(start_idx, cur_sum):
            if start_idx == len(nums):
                return 1 if cur_sum == target else 0
            if (start_idx, cur_sum) in memcache:
                return memcache[(start_idx, cur_sum)]

            add_ways = dfs(start_idx + 1, cur_sum + nums[start_idx])
            sub_ways = dfs(start_idx + 1, cur_sum - nums[start_idx])
            memcache[(start_idx, cur_sum)] = add_ways + sub_ways
            return memcache[(start_idx, cur_sum)]

        return dfs(0, 0)


# @lc code=end
