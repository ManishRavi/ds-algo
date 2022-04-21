/*
 * @lc app=leetcode id=54 lang=golang
 *
 * [54] Spiral Matrix
 */

// @lc code=start
func spiralOrder(matrix [][]int) []int {
	if len(matrix) <= 0 || len(matrix[0]) <= 0 {
		return []int{}
	}

	res, m, n := []int{}, len(matrix), len(matrix[0])
	left, right, top, bottom := 0, n-1, 0, m-1
	for left <= right && top <= bottom {
		// * Traverse from top left corner <=> top right corner
		for j := left; j <= right && len(res) < m*n; j++ {
			res = append(res, matrix[top][j])
		}

		// * Traverse from top right corner <=> bottom right corner
		for i := top + 1; i <= bottom && len(res) < m*n; i++ {
			res = append(res, matrix[i][right])
		}

		// * Traverse from bottom right corner <=> bottom left corner
		for j := right - 1; j >= left && len(res) < m*n; j-- {
			res = append(res, matrix[bottom][j])
		}

		// * Traverse from bottom left corner <=> top left corner
		for i := bottom - 1; i > top && len(res) < m*n; i-- {
			res = append(res, matrix[i][left])
		}

		left++
		right--
		top++
		bottom--
	}

	return res
}

// @lc code=end

