#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start

# * Backtracking Solution | O(mn*(4^w)) Time | O(w) Space
# * m -> The number of rows in the board matrix | n -> The number of columns in the board matrix |
# * w -> The length of the word string


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS, COLS = len(board), len(board[0])
        if ROWS * COLS < len(word):
            return False

        def dfs(row, col, word_idx):
            if word_idx == len(word):
                return True
            if (
                not 0 <= row <= ROWS - 1
                or not 0 <= col <= COLS - 1
                or board[row][col] == "*"
                or board[row][col] != word[word_idx]
            ):
                return False

            cur_val = board[row][col]
            board[row][col] = "*"
            for d_row, d_col in DIRECTIONS:
                if dfs(row + d_row, col + d_col, word_idx + 1):
                    return True

            board[row][col] = cur_val
            return False

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True

        return False


# @lc code=end
