#
# @lc app=leetcode id=967 lang=python3
#
# [967] Numbers With Same Consecutive Differences
#

# @lc code=start

# * Recursive DFS Solution | O(n*(2^n)) Time | O(2^n) Space
# * n -> The given input


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []

        def numsSameConsecDiffHelper(num, digits_left):
            if digits_left == 0:
                res.append(num)
                return

            last_digit = num % 10
            next_num = num * 10 + last_digit
            if 0 <= last_digit - k <= 9:
                numsSameConsecDiffHelper(next_num - k, digits_left - 1)
            if 0 <= last_digit + k <= 9 and k != 0:
                numsSameConsecDiffHelper(next_num + k, digits_left - 1)

        for num in range(1, 10):
            numsSameConsecDiffHelper(num, n - 1)

        return res


# @lc code=end
