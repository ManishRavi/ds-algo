/*
 * @lc app=leetcode id=168 lang=golang
 *
 * [168] Excel Sheet Column Title
 */

// @lc code=start
func convertToTitle(columnNumber int) string {
	res := ""
	for columnNumber > 0 {
		columnNumber--
		res = string(65+(columnNumber)%26) + res
		columnNumber /= 26
	}

	return res
}

// @lc code=end

