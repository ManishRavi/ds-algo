#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start

# * Iterative Solution | O(n) Time | O(n) Space
# * n -> The length of s string


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res, rows_val = [], [[] for _ in range((min(numRows, len(s))))]
        cur_row, is_going_down = 0, False
        for char in s:
            rows_val[cur_row].append(char)
            if cur_row == 0 or cur_row == numRows - 1:
                is_going_down = not is_going_down
            if is_going_down:
                cur_row += 1
            else:
                cur_row -= 1

        for row_val in rows_val:
            res.append("".join(row_val))

        return "".join(res)


# @lc code=end
