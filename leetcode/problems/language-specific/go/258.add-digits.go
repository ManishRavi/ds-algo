/*
 * @lc app=leetcode id=258 lang=golang
 *
 * [258] Add Digits
 */

// @lc code=start
func addDigits(num int) int {
	if num == 0 {
		return num
	}

	return ((num - 1) % 9) + 1
}

// @lc code=end

