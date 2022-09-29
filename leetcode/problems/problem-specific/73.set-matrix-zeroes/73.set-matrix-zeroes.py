#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start

# * Iterative Solution | O(mn) Time | O(1) Space
# * m -> The number of rows in the matrix | n -> The number of columns in the matrix


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        # * 1. Traverse through the whole matrix to capture 0 and set it to * (0 -> *).
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    # * Set the row with *.
                    for c in range(COLS):
                        if matrix[row][c] != 0:
                            matrix[row][c] = "*"
                    # * Set the column with *.
                    for r in range(ROWS):
                        if matrix[r][col] != 0:
                            matrix[r][col] = "*"

        # * 2. Traverse through the whole matrix to unset * and set it to 0 (* -> 0).
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == "*":
                    matrix[row][col] = 0


# @lc code=end
