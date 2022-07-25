/*
 * @lc app=leetcode id=240 lang=golang
 *
 * [240] Search a 2D Matrix II
 */

// @lc code=start

// * Iterative Solution | O(m+n) Time | O(1) Space
// * m -> Number of rows | n -> Number of columns

func searchMatrix(matrix [][]int, target int) bool {
	if len(matrix) <= 0 || len(matrix[0]) <= 0 {
		return false
	}

	ROWS, COLS := len(matrix), len(matrix[0])
	// * Start at first row and last column
	row, col := 0, COLS-1
	for row < ROWS && col >= 0 {
		if matrix[row][col] == target {
			return true
		} else if matrix[row][col] < target {
			row++
		} else {
			col--
		}
	}

	return false
}

// @lc code=end

