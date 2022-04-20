/*
 * @lc app=leetcode id=48 lang=golang
 *
 * [48] Rotate Image
 */

// @lc code=start
func rotate(matrix [][]int) {
	reverse(&matrix)
	transpose(&matrix)
}

func reverse(matrix *[][]int) {
	n := len(*matrix)
	for i := 0; i < n/2; i++ {
		(*matrix)[i], (*matrix)[n-i-1] = (*matrix)[n-i-1], (*matrix)[i]
	}
}

func transpose(matrix *[][]int) {
	for i := 0; i < len(*matrix); i++ {
		for j := 0; j < i; j++ {
			(*matrix)[i][j], (*matrix)[j][i] = (*matrix)[j][i], (*matrix)[i][j]
		}
	}
}

// @lc code=end

