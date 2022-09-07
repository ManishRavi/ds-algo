#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start

# * Backtracking Solution | O(mn*(4^w)) Time | O(w) Space
# * m -> The number of rows in the board matrix | n -> The number of columns in the board matrix
# * w -> The length of the word

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS, COLS = len(board), len(board[0])
        if ROWS * COLS < len(word):
            return False

        def existHelper(row=0, col=0, idx=0):
            if idx == len(word):
                return True

            if (
                not 0 <= row <= ROWS - 1 or
                not 0 <= col <= COLS - 1 or
                board[row][col] != word[idx] or
                board[row][col] == '*'
            ):
                return False

            prev_val = board[row][col]
            board[row][col] = '*'
            is_exist = False
            for d_row, d_col in DIRECTIONS:
                is_exist = is_exist or existHelper(row + d_row, col + d_col, idx + 1)

            board[row][col] = prev_val
            return is_exist

        for row in range(ROWS):
            for col in range(COLS):
                if existHelper(row, col, 0):
                    return True

        return False

# @lc code=end
