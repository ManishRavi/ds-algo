#
# @lc app=leetcode id=980 lang=python3
#
# [980] Unique Paths III
#

# @lc code=start

# * Recursive DFS Solution | O(4^(mn)) Time | O(mn) Space
# * m -> The number of rows in the grid matrix | n -> The number of columns in the grid matrix


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS, COLS = len(grid), len(grid[0])
        start_square = (0, 0)
        res = total_empty_squares = 0

        # * Find the start and empty squares.
        for row in range(ROWS):
            for col in range(COLS):
                total_empty_squares += grid[row][col] == 0
                if grid[row][col] == 1:
                    start_square = (row, col)
                    total_empty_squares += 1

        def dfs(row, col):
            nonlocal res, total_empty_squares

            if (
                not 0 <= row <= ROWS - 1
                or not 0 <= col <= COLS - 1
                or grid[row][col] == -1
            ):
                return
            if grid[row][col] == 2:
                res += total_empty_squares == 0
                return

            cur_val = grid[row][col]
            grid[row][col] = -1
            total_empty_squares -= 1
            for d_row, d_col in DIRECTIONS:
                dfs(row + d_row, col + d_col)

            grid[row][col] = cur_val
            total_empty_squares += 1

        dfs(*start_square)
        return res


# @lc code=end
