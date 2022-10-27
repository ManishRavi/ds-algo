#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start

# * Hash Table Solution | O(n) Time | O(min(n, k)) Space
# * n -> The length of nums array | k -> The given input


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # * Key -> Sum | Value -> Index
        nums_sum_idx_map = {0: 0}
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            # * If the remainder cur_sum % k occurs for the first time.
            if cur_sum % k not in nums_sum_idx_map:
                nums_sum_idx_map[cur_sum % k] = i + 1
            # * If the subarray size is at least two.
            elif nums_sum_idx_map[cur_sum % k] < i:
                return True

        return False


# @lc code=end
