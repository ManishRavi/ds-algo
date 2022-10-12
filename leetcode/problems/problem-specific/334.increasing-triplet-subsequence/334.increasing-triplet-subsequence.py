#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start

# * Greedy Solution | O(n) Time | O(1) Space
# * n -> The length of nums array


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_val_1 = min_val_2 = float("inf")
        for num in nums:
            min_val_1 = min(min_val_1, num)
            if num > min_val_2:
                return True
            elif num > min_val_1:
                min_val_2 = num

        return False


# @lc code=end
