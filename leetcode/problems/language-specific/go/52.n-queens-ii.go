/*
 * @lc app=leetcode id=52 lang=golang
 *
 * [52] N-Queens II
 */

// @lc code=start

// * Backtracking Solution | O(n^2) Time | O(n^2) Space

func totalNQueens(n int) int {
	res := 0
	leftRow, lowerDiagonal, upperDiagonal := make([]int, n), make([]int, 2*n-1), make([]int, 2*n-1)
	board := make([]string, n)
	var emptyBoardSB strings.Builder
	for i := 0; i < n; i++ {
		emptyBoardSB.WriteString(".")
	}
	for i := range board {
		board[i] = emptyBoardSB.String()
	}

	var totalNQueensHelper func(col int)
	totalNQueensHelper = func(col int) {
		if col == n {
			res++
		}

		for row := 0; row < n; row++ {
			if leftRow[row] == 0 &&
				lowerDiagonal[row+col] == 0 &&
				upperDiagonal[n-1+col-row] == 0 {
				board[row] = fmt.Sprintf("%vQ%v", board[row][:col], board[row][col+1:])
				leftRow[row] = 1
				lowerDiagonal[row+col] = 1
				upperDiagonal[n-1+col-row] = 1
				totalNQueensHelper(col + 1)
				board[row] = fmt.Sprintf("%v.%v", board[row][:col], board[row][col+1:])
				leftRow[row] = 0
				lowerDiagonal[row+col] = 0
				upperDiagonal[n-1+col-row] = 0
			}
		}
	}

	totalNQueensHelper(0)
	return res
}

// @lc code=end

