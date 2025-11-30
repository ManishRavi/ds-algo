#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start

# * Recursive DFS Solution | O(mn) Time | O(mn) Space
# * m -> The number of rows in the matrix | n -> The number of columns in the matrix


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS, COLS = len(matrix), len(matrix[0])
        memcache = [[1] * COLS for _ in range(ROWS)]

        def helper(row, col, prev_val):
            if (
                not 0 <= row <= ROWS - 1
                or not 0 <= col <= COLS - 1
                or matrix[row][col] <= prev_val
            ):
                return 0
            if memcache[row][col] != 1:
                return memcache[row][col]

            cur_len = 0
            for d_row, d_col in DIRECTIONS:
                cur_len = max(
                    cur_len, helper(row + d_row, col + d_col, matrix[row][col])
                )

            memcache[row][col] = 1 + cur_len
            return memcache[row][col]

        max_len = 0
        for row in range(ROWS):
            for col in range(COLS):
                max_len = max(max_len, helper(row, col, -1))

        return max_len


# @lc code=end
