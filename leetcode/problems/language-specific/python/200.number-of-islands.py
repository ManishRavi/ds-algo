#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start

# * Recursive DFS Solution | O(mn) Time | O(1) Space
# * m -> The number of rows in the grid matrix | n -> The number of columns in the grid matrix

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS, COLS = len(grid), len(grid[0])

        def numIslandsHelper(row, col):
            if (
                not 0 <= row <= ROWS - 1 or
                not 0 <= col <= COLS - 1 or
                grid[row][col] == '0'
            ):
                return

            grid[row][col] = '0'
            for d_row, d_col in DIRECTIONS:
                numIslandsHelper(row + d_row, col + d_col)

        no_of_islands = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    numIslandsHelper(row, col)
                    no_of_islands += 1

        return no_of_islands

# @lc code=end
