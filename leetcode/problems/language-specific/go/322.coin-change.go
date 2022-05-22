/*
 * @lc app=leetcode id=322 lang=golang
 *
 * [322] Coin Change
 */

// @lc code=start

// * Bottom-Up Iterative Solution | O(ca) Time | O(a) Space

func coinChange(coins []int, amount int) int {
	if len(coins) <= 0 || amount == 0 {
		return 0
	}

	dp := make([]int, amount+1)
	for i := 1; i < len(dp); i++ {
		dp[i] = amount + 1
	}

	for _, v := range coins {
		for i := v; i < len(dp); i++ {
			dp[i] = findMin(dp[i], 1+dp[i-v])
		}
	}

	if dp[amount] <= amount {
		return dp[amount]
	}

	return -1
}

func findMin(a, b int) int {
	if a <= b {
		return a
	}

	return b
}

// @lc code=end

