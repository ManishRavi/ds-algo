/*
 * @lc app=leetcode id=441 lang=golang
 *
 * [441] Arranging Coins
 */

// @lc code=start
func arrangeCoins(n int) int {
	if n <= 2 {
		return 1
	}

	currentRow := 1
	for n >= currentRow {
		n -= currentRow
		currentRow++
	}

	return currentRow - 1
}

// @lc code=end

