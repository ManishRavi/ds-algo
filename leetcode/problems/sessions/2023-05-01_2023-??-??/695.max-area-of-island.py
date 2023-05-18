#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start

# * Recursive DFS Solution | O(mn) Time | O(1) Space
# * m -> The number of rows in the grid matrix | n -> The number of columns in the grid matrix


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row, col):
            if (
                not 0 <= row <= ROWS - 1
                or not 0 <= col <= COLS - 1
                or grid[row][col] == 0
            ):
                return 0

            grid[row][col] = 0
            cur_area = 0
            for d_row, d_col in DIRECTIONS:
                cur_area += dfs(row + d_row, col + d_col)

            return 1 + cur_area

        max_area = 0
        for row in range(ROWS):
            for col in range(COLS):
                max_area = max(max_area, dfs(row, col))

        return max_area


# @lc code=end
