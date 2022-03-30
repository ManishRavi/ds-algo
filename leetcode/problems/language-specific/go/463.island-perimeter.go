/*
 * @lc app=leetcode id=463 lang=golang
 *
 * [463] Island Perimeter
 */

// @lc code=start
func islandPerimeter(grid [][]int) int {
	if len(grid) <= 0 || len(grid[0]) <= 0 {
		return 0
	}

	res, row, col := 0, len(grid), len(grid[0])
	for i := 0; i < row; i++ {
		for j := 0; j < col; j++ {
			if grid[i][j] == 0 {
				continue
			}
			if i == 0 || grid[i-1][j] == 0 {
				res++
			}
			if i == row-1 || grid[i+1][j] == 0 {
				res++
			}
			if j == 0 || grid[i][j-1] == 0 {
				res++
			}
			if j == col-1 || grid[i][j+1] == 0 {
				res++
			}
		}
	}

	return res
}

// @lc code=end

