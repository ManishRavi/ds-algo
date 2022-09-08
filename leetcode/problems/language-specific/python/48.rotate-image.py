#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start

# * Iterative Solution | O(n^2) Time | O(1) Space
# * n -> The number of rows and columns in the matrix


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reverse(matrix)

    def transpose(self, matrix: List[List[int]]) -> None:
        """
        Transposes the input matrix in-place.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        for row in range(ROWS):
            for col in range(row + 1, COLS):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    def reverse(self, matrix: List[List[int]]) -> None:
        """
        Reverses each row in the input matrix in-place.
        """
        for row in range(len(matrix)):
            matrix[row].reverse()


# @lc code=end
