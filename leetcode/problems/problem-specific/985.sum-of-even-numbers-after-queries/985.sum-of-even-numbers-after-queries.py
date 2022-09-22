#
# @lc app=leetcode id=985 lang=python3
#
# [985] Sum of Even Numbers After Queries
#

# @lc code=start

# * Math Solution | O(n) Time | O(1) Space
# * n -> The length of nums or queries array


class Solution:
    def sumEvenAfterQueries(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        res = []
        total_even_sum = sum(num for num in nums if not num % 2)
        for val, idx in queries:
            # * If the previous number is even.
            if not nums[idx] % 2:
                total_even_sum -= nums[idx]
            nums[idx] += val
            # * If the updated number is even.
            if not nums[idx] % 2:
                total_even_sum += nums[idx]
            res.append(total_even_sum)

        return res


# @lc code=end
