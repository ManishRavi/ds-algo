#
# @lc app=leetcode id=1706 lang=python3
#
# [1706] Where Will the Ball Fall
#

# @lc code=start

# * Recursive DFS Solution | O(mn) Time | O(m) Space
# * m -> The number of rows in the grid matrix | n -> The number of columns in the grid matrix


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ROWS, COLS = len(grid), len(grid[0])

        def findBallHelper(row, col):
            if row >= ROWS:
                return col

            # * Ball moving from left to right.
            if grid[row][col] == 1 and col + 1 <= COLS - 1 and grid[row][col + 1] == 1:
                return findBallHelper(row + 1, col + 1)
            # * Ball moving from right to left.
            if grid[row][col] == -1 and col - 1 >= 0 and grid[row][col - 1] == -1:
                return findBallHelper(row + 1, col - 1)
            # * OOB.
            else:
                return -1

        res = [-1] * COLS
        for col in range(COLS):
            res[col] = findBallHelper(0, col)

        return res


# @lc code=end
