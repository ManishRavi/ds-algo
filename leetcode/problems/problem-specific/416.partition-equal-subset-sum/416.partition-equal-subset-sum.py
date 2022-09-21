#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start

# * Iterative Bottom-Up Solution | O(n*(sum(nums))) Time | O(sum(nums)) Space
# * n -> The length of nums array


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_total_sum = sum(nums)
        nums_half_sum = nums_total_sum // 2
        # * We can't partition if the total sum is odd.
        if nums_total_sum % 2:
            return False

        nums_set = set([0])
        for num in nums:
            cur_nums_set = nums_set.copy()
            for v in nums_set:
                if v + num == nums_half_sum:
                    return True

                cur_nums_set.add(v + num)
            nums_set = cur_nums_set

        return False


# @lc code=end
