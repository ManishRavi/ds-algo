/*
 * @lc app=leetcode id=459 lang=golang
 *
 * [459] Repeated Substring Pattern
 */

// @lc code=start
func repeatedSubstringPattern(s string) bool {
	for i := len(s) / 2; i >= 1; i-- {
		if len(s)%i == 0 && strings.Repeat(s[:i], len(s)/i) == s {
			return true
		}
	}

	return false
}

// @lc code=end

