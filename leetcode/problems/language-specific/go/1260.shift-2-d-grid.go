/*
 * @lc app=leetcode id=1260 lang=golang
 *
 * [1260] Shift 2D Grid
 */

// @lc code=start
func shiftGrid(grid [][]int, k int) [][]int {
	m, n := len(grid), len(grid[0])
	res := make([][]int, m)
	for i := 0; i < m; i++ {
		res[i] = make([]int, n)
	}

	for row := range grid {
		for col := range grid[row] {
			newSwiftedPosIn1D := (posToVal(row, col, n) + k) % (m * n)
			newRow, newCol := valToPos(newSwiftedPosIn1D, n)
			res[newRow][newCol] = grid[row][col]
		}
	}

	return res
}

// posToVal returns the corresponding index position/val to be mapped in 1D array
func posToVal(row, col, n int) int {
	return row*n + col
}

// valToPos returns the corresponding position (row and col) in 2D array from 1D array
func valToPos(val, n int) (int, int) {
	return int(val / n), val % n
}

// @lc code=end

