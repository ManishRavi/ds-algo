#
# @lc app=leetcode id=1329 lang=python3
#
# [1329] Sort the Matrix Diagonally
#

# @lc code=start

# * Iterative Sorting Solution | O(m*n*log(min(m, n)) Time | O(mn) Space
# * m -> The number of rows in the matrix | n -> The number of columns in the matrix

class Solution:
    def get_diagonal_elements(self, matrix, row, col, ROWS, COLS):
        diagonal = []
        for i, j in zip(range(row, ROWS), range(col, COLS)):
            diagonal.append(matrix[i][j])

        return diagonal

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])

        # * In the first row, col goes through the whole row,
        # * but in the subsequent rows it only goes on the first column.
        for row in range(ROWS):
            for col in range(1 if row else COLS):
                # * Get the diagonal elements.
                diagonal = self.get_diagonal_elements(
                    mat, row, col, ROWS, COLS
                )

                diagonal.sort()
                # * Put the sorted elements back to their respective positions in the given matrix.
                for i, j, k in zip(range(row, ROWS), range(col, COLS), range(len(diagonal))):
                    mat[i][j] = diagonal[k]

        return mat

# @lc code=end
