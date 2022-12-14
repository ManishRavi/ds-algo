#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#

# @lc code=start

# * Iterative Bottom-Up Solution | O(mn) Time | O(1) Space
# * m -> The number of rows in the matrix | n -> The number of columns in the matrix


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        for row in range(ROWS - 2, -1, -1):
            for col in range(COLS):
                left_diagonal = matrix[row + 1][col - 1] if col > 0 else float("inf")
                bottom = matrix[row + 1][col]
                right_diagonal = (
                    matrix[row + 1][col + 1] if col < COLS - 1 else float("inf")
                )

                matrix[row][col] += min(left_diagonal, bottom, right_diagonal)

        return min(matrix[0])


# @lc code=end
