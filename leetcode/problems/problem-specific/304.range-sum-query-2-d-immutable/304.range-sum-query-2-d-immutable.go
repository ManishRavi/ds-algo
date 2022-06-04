package main

// * Prefix Sum Solution | O(mn) Time Pre-computation | O(1) Time Per Query | O(mn) Space

type NumMatrix struct {
	DP [][]int
}

func Constructor(matrix [][]int) NumMatrix {
	if len(matrix) <= 0 || len(matrix[0]) <= 0 {
		return NumMatrix{}
	}

	ROWS, COLS := len(matrix), len(matrix[0])
	obj := NumMatrix{make([][]int, ROWS+1)}
	for i := range obj.DP {
		obj.DP[i] = make([]int, COLS+1)
	}

	for row := 0; row < ROWS; row++ {
		prefixSum := 0
		for col := 0; col < COLS; col++ {
			prefixSum += matrix[row][col]
			aboveSum := obj.DP[row][col+1]
			obj.DP[row+1][col+1] = prefixSum + aboveSum
		}
	}

	return obj
}

func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
	row1++
	col1++
	row2++
	col2++
	bottomRightSum := this.DP[row2][col2]
	aboveSum := this.DP[row1-1][col2]
	leftSum := this.DP[row2][col1-1]
	topLeftSum := this.DP[row1-1][col1-1]

	return bottomRightSum - aboveSum - leftSum + topLeftSum
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * obj := Constructor(matrix);
 * param_1 := obj.SumRegion(row1,col1,row2,col2);
 */
