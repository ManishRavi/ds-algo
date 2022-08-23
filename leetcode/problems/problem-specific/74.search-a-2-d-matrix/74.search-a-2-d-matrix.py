#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start

# * Binary Search Solution | O(log(mn)) Time | O(1) Space
# * m -> The number of rows in a matrix | n -> The number of columns in a matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # * val_to_pos returns the corresponding position (row and col) in 2D array from 1D array
        def val_to_pos(val):
            return (val // COLS), (val % COLS)

        ROWS, COLS = len(matrix), len(matrix[0])
        left, right = 0, (ROWS * COLS) - 1
        while left <= right:
            mid = left + (right - left) // 2
            row, col = val_to_pos(mid)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

# @lc code=end
