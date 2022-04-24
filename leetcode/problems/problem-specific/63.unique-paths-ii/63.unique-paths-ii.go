package main

func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	if len(obstacleGrid) <= 0 || len(obstacleGrid[0]) <= 0 || obstacleGrid[0][0] == 1 {
		return 0
	}

	m, n := len(obstacleGrid), len(obstacleGrid[0])
	dp := make([]int, n)
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if obstacleGrid[i][j] == 1 {
				dp[j] = 0
			} else if i == 0 && j == 0 {
				dp[j] = 1
			} else if j > 0 {
				dp[j] += dp[j-1]
			}
		}
	}

	return dp[n-1]
}
