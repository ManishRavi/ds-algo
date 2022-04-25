package main

func minPathSum(grid [][]int) int {
	if len(grid) == 0 || len(grid[0]) == 0 {
		return 0
	}

	m, n := len(grid), len(grid[0])
	dp := make([]int, n)
	for i := 0; i < n; i++ {
		if i == 0 {
			dp[i] = grid[0][i]
		} else {
			dp[i] = dp[i-1] + grid[0][i]
		}
	}

	for i := 1; i < m; i++ {
		for j := 0; j < n; j++ {
			if j == 0 {
				dp[j] += grid[i][j]
			} else {
				dp[j] = findMin(dp[j], dp[j-1]) + grid[i][j]
			}
		}
	}

	return dp[n-1]
}

func findMin(a, b int) int {
	if a <= b {
		return a
	}

	return b
}
