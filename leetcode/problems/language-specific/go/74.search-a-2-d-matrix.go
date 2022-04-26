/*
 * @lc app=leetcode id=74 lang=golang
 *
 * [74] Search a 2D Matrix
 */

// @lc code=start
func searchMatrix(matrix [][]int, target int) bool {
	if len(matrix) <= 0 || len(matrix[0]) <= 0 {
		return false
	}

	m, n := len(matrix), len(matrix[0])
	left, right := 0, m*n-1
	for left <= right {
		mid := left + (right-left)/2
		row, col := valToPos(mid, n)
		if matrix[row][col] == target {
			return true
		} else if matrix[row][col] < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return false
}

// valToPos returns the corresponding position (row and col) in 2D array from 1D array
func valToPos(val, n int) (int, int) {
	return int(val / n), val % n
}

// @lc code=end

