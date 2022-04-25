/*
 * @lc app=leetcode id=73 lang=golang
 *
 * [73] Set Matrix Zeroes
 */

// @lc code=start
func setZeroes(matrix [][]int) {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return
	}

	m, n := len(matrix), len(matrix[0])
	isFirstRowZero, isFirstColZero := false, false
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if matrix[i][j] == 0 {
				if i == 0 {
					isFirstRowZero = true
				}
				if j == 0 {
					isFirstColZero = true
				}

				matrix[i][0] = 0
				matrix[0][j] = 0
			}
		}
	}

	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			if matrix[i][0] == 0 || matrix[0][j] == 0 {
				matrix[i][j] = 0
			}
		}
	}

	if isFirstRowZero {
		for j := 0; j < n; j++ {
			matrix[0][j] = 0
		}
	}
	if isFirstColZero {
		for i := 0; i < m; i++ {
			matrix[i][0] = 0
		}
	}
}

// @lc code=end

