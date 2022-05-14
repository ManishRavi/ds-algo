/*
 * @lc app=leetcode id=37 lang=golang
 *
 * [37] Sudoku Solver
 */

// @lc code=start

// * Backtracking Solution | O(9^(m*n)) Time | O(1) Space

func solveSudoku(board [][]byte) {
	ROWS, COLS := len(board), len(board[0])
	var isValidSudoku func(row, col int, c byte) bool
	isValidSudoku = func(row, col int, c byte) bool {
		for i := 0; i < 9; i++ {
			if board[row][i] == c ||
				board[i][col] == c ||
				board[(3*(row/3))+(i/3)][(3*(col/3)+(i%3))] == c {
				return false
			}
		}

		return true
	}

	var solveSudokuHelper func() bool
	solveSudokuHelper = func() bool {
		// * Search for an empty cell in the board
		for row := 0; row < ROWS; row++ {
			for col := 0; col < COLS; col++ {
				if board[row][col] == '.' {
					for c := '1'; c <= '9'; c++ {
						if isValidSudoku(row, col, byte(c)) {
							board[row][col] = byte(c)
							if solveSudokuHelper() {
								return true
							} else {
								board[row][col] = '.'
							}
						}
					}

					return false
				}
			}
		}

		return true
	}

	solveSudokuHelper()
}

// @lc code=end

