#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start

# * Binary Search Solution | O(log(mn)) Time | O(1) Space
# * m -> The number of rows in the matrix | n -> The number of columns in the matrix


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        def get_val_to_pos(val):
            """Returns the corresponding position (row and col) in 2D array from 1D array."""
            return (val // COLS), (val % COLS)

        left, right = 0, (ROWS * COLS) - 1
        while left <= right:
            mid = left + (right - left) // 2
            row, col = get_val_to_pos(mid)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


# @lc code=end
