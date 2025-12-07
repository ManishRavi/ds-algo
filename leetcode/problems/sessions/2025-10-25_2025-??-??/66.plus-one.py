#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start

# * Math Solution | O(n) Time | O(1) Space
# * n -> The length of digits array


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            carry, digits[i] = divmod(1 + digits[i], 10)
            if not carry:
                return digits

        return digits if not carry else [1] + digits


# @lc code=end
