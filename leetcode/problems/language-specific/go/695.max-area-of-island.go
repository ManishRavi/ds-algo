/*
 * @lc app=leetcode id=695 lang=golang
 *
 * [695] Max Area of Island
 */

// @lc code=start

// * Recursive DFS Solution | O(rc) Time | O(rc) Space
// * r -> Total number of rows in a grid matrix | c -> Total number of cols in a grid matrix

func maxAreaOfIsland(grid [][]int) int {
	ROWS, COLS := len(grid), len(grid[0])
	maxArea, seen := 0, make([][]bool, ROWS)
	for i := 0; i < ROWS; i++ {
		seen[i] = make([]bool, COLS)
	}

	var maxAreaOfIslandHelper func(row, col int) int
	maxAreaOfIslandHelper = func(row, col int) int {
		if row < 0 || row > ROWS-1 ||
			col < 0 || col > COLS-1 ||
			seen[row][col] || grid[row][col] == 0 {
			return 0
		}

		seen[row][col] = true
		return 1 + (maxAreaOfIslandHelper(row-1, col) + maxAreaOfIslandHelper(row+1, col) + maxAreaOfIslandHelper(row, col-1) + maxAreaOfIslandHelper(row, col+1))
	}

	for row := 0; row < ROWS; row++ {
		for col := 0; col < COLS; col++ {
			maxArea = findMax(maxArea, maxAreaOfIslandHelper(row, col))
		}
	}

	return maxArea
}

func findMax(a, b int) int {
	if a >= b {
		return a
	}

	return b
}

// @lc code=end

