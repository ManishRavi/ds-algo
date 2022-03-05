/*
 * @lc app=leetcode id=58 lang=golang
 *
 * [58] Length of Last Word
 */

// @lc code=start
func lengthOfLastWord(s string) int {
	if len(s) <= 0 {
		return 0
	}

	count := 0
	s = strings.Trim(s, " ")
	for i := len(s) - 1; i >= 0; i-- {
		if s[i] == ' ' {
			break
		}
		count++
	}

	return count
}

// @lc code=end

