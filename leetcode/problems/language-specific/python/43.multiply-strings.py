#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start

# * Math Solution | O(mn) Time | O(m+n) Space
# * m -> The length of num1 string | n -> The length of num2 string


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for j, digit2 in enumerate(num2):
            # * For each digit in num2 multiply the digit by all digits in num1.
            for i, digit1 in enumerate(num1):
                # * Multiply the current digits and add the carry.
                cur_digit = int(digit1) * int(digit2) + res[i + j]
                # * Set the one's place of the multiplication result.
                res[i + j] = cur_digit % 10
                # * Carry the tens place of the multiplication result by
                # * adding it to the next position in the result array.
                res[i + j + 1] += cur_digit // 10

        # * Pop the excess 0 from the end of the result.
        if res[-1] == 0:
            res.pop()

        return "".join([str(digit) for digit in res[::-1]])


# @lc code=end
