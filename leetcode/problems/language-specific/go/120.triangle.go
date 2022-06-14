/*
 * @lc app=leetcode id=120 lang=golang
 *
 * [120] Triangle
 */

// @lc code=start

// * Bottom-Up Iterative Solution | O(mn) Time | O(m) Space

func minimumTotal(triangle [][]int) int {
	if len(triangle) <= 0 || len(triangle[0]) <= 0 {
		return 0
	}

	ROWS := len(triangle)
	dp := make([]int, ROWS+1)
	for row := ROWS - 1; row >= 0; row-- {
		for i, v := range triangle[row] {
			dp[i] = findMin(dp[i], dp[i+1]) + v
		}
	}

	return dp[0]
}

func findMin(a, b int) int {
	if a <= b {
		return a
	}

	return b
}

// @lc code=end

