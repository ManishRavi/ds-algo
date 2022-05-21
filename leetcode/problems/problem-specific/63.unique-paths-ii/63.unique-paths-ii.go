package main

// * Dynamic Programming Solution | O(mn) Time | O(n) Space

func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	if len(obstacleGrid) <= 0 || len(obstacleGrid[0]) <= 0 || obstacleGrid[0][0] == 1 {
		return 0
	}

	ROWS, COLS := len(obstacleGrid), len(obstacleGrid[0])
	dp := make([]int, COLS)
	for i := 0; i < ROWS; i++ {
		for j := 0; j < COLS; j++ {
			if obstacleGrid[i][j] == 1 {
				dp[j] = 0
			} else if i == 0 && j == 0 {
				dp[j] = 1
			} else if j > 0 {
				dp[j] += dp[j-1]
			}
		}
	}

	return dp[COLS-1]
}
