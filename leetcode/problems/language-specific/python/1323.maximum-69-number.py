#
# @lc app=leetcode id=1323 lang=python3
#
# [1323] Maximum 69 Number
#

# @lc code=start

# * Math Solution | O(n) Time | O(n) Space
# * n -> The number of digits in num integer


class Solution:
    def maximum69Number(self, num: int) -> int:
        num_char_list = list(str(num))
        for idx, num_char in enumerate(num_char_list):
            if num_char == "6":
                num_char_list[idx] = "9"
                break

        return int("".join(num_char_list))


# @lc code=end
