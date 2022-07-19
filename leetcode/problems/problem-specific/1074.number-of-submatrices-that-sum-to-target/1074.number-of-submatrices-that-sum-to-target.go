package main

/*
 * @lc app=leetcode id=1074 lang=golang
 *
 * [1074] Number of Submatrices That Sum to Target
 */

// @lc code=start

// * Prefix Sum Solution | O(m*(n^2)) Time | O(n) Space
// * m -> Total number of rows in a matrix | n -> Total number of columns in a matrix

func numSubmatrixSumTarget(matrix [][]int, target int) int {
	ROWS, COLS := len(matrix), len(matrix[0])
	// * Build prefix sum
	for row := 0; row < ROWS; row++ {
		for col := 1; col < COLS; col++ {
			matrix[row][col] += matrix[row][col-1]
		}
	}

	res := 0
	for col1 := 0; col1 < COLS; col1++ {
		for col2 := col1; col2 < COLS; col2++ {
			mappings := map[int]int{0: 1}
			totalSum := 0
			for row := 0; row < ROWS; row++ {
				prevElement := 0
				if col1 > 0 {
					prevElement = matrix[row][col1-1]
				}

				totalSum += matrix[row][col2] - prevElement
				if occurrenceVal, ok := mappings[totalSum-target]; ok {
					res += occurrenceVal
				}

				mappings[totalSum]++
			}
		}
	}

	return res
}

// @lc code=end
