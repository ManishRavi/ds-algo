#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start

# * Backtracking Solution | O((n^2)*n!) Time | O(n^2) Space
# * n -> The given input


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col_set = set()
        # * row + col will be constant.
        positive_diagonal_set = set()
        # * row - col will be constant.
        negative_diagonal_set = set()
        # * board -> When n = 3 -> [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
        board = [["."] * n for _ in range(n)]
        res = []

        def solveNQueensHelper(row):
            if row == n:
                res.append(["".join(row_val) for row_val in board])
                return

            for col in range(n):
                if (
                    col in col_set
                    or (row + col) in positive_diagonal_set
                    or (row - col) in negative_diagonal_set
                ):
                    continue

                col_set.add(col)
                positive_diagonal_set.add(row + col)
                negative_diagonal_set.add(row - col)
                board[row][col] = "Q"
                solveNQueensHelper(row + 1)
                col_set.remove(col)
                positive_diagonal_set.remove(row + col)
                negative_diagonal_set.remove(row - col)
                board[row][col] = "."

        solveNQueensHelper(0)
        return res


# @lc code=end
