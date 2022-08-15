#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start

# * Hash Table Solution | O(rc) Time | O(rc) Space
# * r -> The number of rows in the board array | c -> The number of columns in the board array

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        mappings_set = set()
        for row in range(ROWS):
            for col in range(COLS):
                cur_val = board[row][col]
                if cur_val != ".":
                    if (
                        (f'r{row}', cur_val) in mappings_set or
                        (f'c{col}', cur_val) in mappings_set or
                        (f'b{row//3}{col//3}', cur_val) in mappings_set
                    ):
                        return False

                    mappings_set.add((f'r{row}', cur_val))
                    mappings_set.add((f'c{col}', cur_val))
                    mappings_set.add((f'b{row//3}{col//3}', cur_val))

        return True

# @lc code=end
