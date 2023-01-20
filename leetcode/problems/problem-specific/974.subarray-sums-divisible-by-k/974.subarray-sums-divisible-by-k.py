#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#

# @lc code=start

# * Hash Table and Prefix Sum Solution | O(n) Time | O(k) Space
# * n -> The length of nums array | k -> The given input


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_cnt_map = defaultdict(int)
        remainder_cnt_map[0] = 1
        cur_sum = res = 0
        for num in nums:
            cur_sum += num
            rem = cur_sum % k
            if rem < 0:
                rem += k

            res += remainder_cnt_map[rem]
            remainder_cnt_map[rem] += 1

        return res


# @lc code=end
