#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start

# * Recursive DFS Solution | O(mn) Time | O(1) Space
# * m -> The number of rows in the board matrix | n -> The number of columns in the board matrix


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS, COLS = len(board), len(board[0])

        def helper(row, col):
            if (
                not 0 <= row <= ROWS - 1
                or not 0 <= col <= COLS - 1
                or board[row][col] != "O"
            ):
                return

            board[row][col] = "*"
            for d_row, d_col in DIRECTIONS:
                helper(row + d_row, col + d_col)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O" and (
                    row in (0, ROWS - 1) or col in (0, COLS - 1)
                ):
                    helper(row, col)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "*":
                    board[row][col] = "O"


# @lc code=end
