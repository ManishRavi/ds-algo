#
# @lc app=leetcode id=766 lang=python3
#
# [766] Toeplitz Matrix
#

# @lc code=start

# * Math Solution | O(mn) Time | O(1) Space
# * m -> The number of rows in the matrix | n -> The number of columns in the matrix


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        # * Compare with the top-left neighbor.
        for row in range(ROWS):
            for col in range(COLS):
                if row and col and matrix[row][col] != matrix[row - 1][col - 1]:
                    return False

        return True


# @lc code=end
