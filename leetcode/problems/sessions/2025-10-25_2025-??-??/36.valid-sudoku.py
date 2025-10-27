#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start

# * Hash Table Solution | O(mn) Time | O(mn) Space
# * m -> The number of rows in the board matrix | n -> The number of columns in the board matrix


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        board_set = set()
        for row in range(ROWS):
            for col in range(COLS):
                cur_val = board[row][col]
                if cur_val != ".":
                    if (
                        (f"r#{row}", cur_val) in board_set
                        or (f"c#{col}", cur_val) in board_set
                        or (f"sb#{row // 3}{col // 3}", cur_val) in board_set
                    ):
                        return False

                    board_set.add((f"r#{row}", cur_val))
                    board_set.add((f"c#{col}", cur_val))
                    board_set.add((f"sb#{row // 3}{col // 3}", cur_val))

        return True


# @lc code=end
