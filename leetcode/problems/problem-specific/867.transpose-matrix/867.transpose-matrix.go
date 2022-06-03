package main

// * Iterative Solution | O(mn) Time | O(mn) Space

func transpose(matrix [][]int) [][]int {
	if len(matrix) <= 0 || len(matrix[0]) <= 0 {
		return matrix
	}

	ROWS, COLS := len(matrix), len(matrix[0])
	res := make([][]int, COLS)
	for i := range res {
		res[i] = make([]int, ROWS)
	}

	for i := 0; i < ROWS; i++ {
		for j := 0; j < COLS; j++ {
			res[j][i] = matrix[i][j]
		}
	}

	return res
}
