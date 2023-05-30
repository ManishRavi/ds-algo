#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start

# * Math Solution | O(mn) Time | O(1) Space
# * m -> The number of rows in the given matrix | n -> The number of columns in the given matrix


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self._transpose(matrix)
        self._reverse(matrix)

    def _transpose(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        for row in range(ROWS):
            for col in range(row + 1, COLS):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    def _reverse(self, matrix: List[List[int]]):
        for row in matrix:
            row.reverse()


# @lc code=end
