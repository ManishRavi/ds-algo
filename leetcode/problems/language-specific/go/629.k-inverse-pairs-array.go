/*
 * @lc app=leetcode id=629 lang=golang
 *
 * [629] K Inverse Pairs Array
 */

// @lc code=start

// * Bottom-Up Iterative Solution | O(nk) Time | O(k) Space
// * n -> Total length of the array | k -> Number of inverse pairs in an array

func kInversePairs(n int, k int) int {
	prevDP := make([]int, k+1)
	dp := make([]int, k+1)
	dp[0] = 1

	for i := 2; i <= n; i++ {
		prevDP, dp = dp, prevDP
		sum := 0

		for j := range dp {
			sum += prevDP[j]

			if j >= i {
				sum -= prevDP[j-i]
			}

			dp[j] = sum % 1_000_000_007
		}
	}

	return dp[k]
}

// @lc code=end

