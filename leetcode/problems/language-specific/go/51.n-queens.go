/*
 * @lc app=leetcode id=51 lang=golang
 *
 * [51] N-Queens
 */

// @lc code=start

// * Backtracking Solution | O(n^2) Time | O(n^2) Space

func solveNQueens(n int) [][]string {
	res := [][]string{}
	leftRow, lowerDiagonal, upperDiagonal := make([]int, n), make([]int, 2*n-1), make([]int, 2*n-1)
	board := make([]string, n)
	var emptyBoardSB strings.Builder
	for i := 0; i < n; i++ {
		emptyBoardSB.WriteString(".")
	}
	for i := range board {
		board[i] = emptyBoardSB.String()
	}

	var solveNQueensHelper func(col int)
	solveNQueensHelper = func(col int) {
		if col == n {
			res = append(res, append([]string{}, board...))
		}

		for row := 0; row < n; row++ {
			if leftRow[row] == 0 &&
				lowerDiagonal[row+col] == 0 &&
				upperDiagonal[n-1+col-row] == 0 {
				board[row] = fmt.Sprintf("%vQ%v", board[row][:col], board[row][col+1:])
				leftRow[row] = 1
				lowerDiagonal[row+col] = 1
				upperDiagonal[n-1+col-row] = 1
				solveNQueensHelper(col + 1)
				board[row] = fmt.Sprintf("%v.%v", board[row][:col], board[row][col+1:])
				leftRow[row] = 0
				lowerDiagonal[row+col] = 0
				upperDiagonal[n-1+col-row] = 0
			}
		}
	}

	solveNQueensHelper(0)
	return res
}

// @lc code=end

