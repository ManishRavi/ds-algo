/*
 * @lc app=leetcode id=392 lang=golang
 *
 * [392] Is Subsequence
 */

// @lc code=start
func isSubsequence(s string, t string) bool {
	if len(s) > len(t) {
		return false
	}

	i, j := 0, 0
	for i < len(s) && j < len(t) {
		if s[i] != t[j] {
			j++
		} else {
			i++
			j++
		}
	}

	if i == len(s) {
		return true
	}

	return false
}

// @lc code=end

