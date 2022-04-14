/*
 * @lc app=leetcode id=59 lang=golang
 *
 * [59] Spiral Matrix II
 */

// @lc code=start
func generateMatrix(n int) [][]int {
	res, element := make([][]int, n), 1
	left, right, top, bottom := 0, n-1, 0, n-1
	for i := 0; i < n; i++ {
		res[i] = make([]int, n)
	}

	for left <= right && top <= bottom {
		// * Traverse from top left corner <=> top right corner
		for j := left; j <= right; j++ {
			res[top][j] = element
			element++
		}

		// * Traverse from top right corner <=> bottom right corner
		for i := top + 1; i <= bottom; i++ {
			res[i][right] = element
			element++
		}

		// * Traverse from bottom right corner <=> bottom left corner
		for j := right - 1; j >= left; j-- {
			res[bottom][j] = element
			element++
		}

		// * Traverse from bottom left corner <=> top left corner
		for i := bottom - 1; i > top; i-- {
			res[i][left] = element
			element++
		}

		left++
		right--
		top++
		bottom--
	}

	return res
}

// @lc code=end

