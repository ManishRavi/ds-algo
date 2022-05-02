/*
 * @lc app=leetcode id=844 lang=golang
 *
 * [844] Backspace String Compare
 */

// @lc code=start
func backspaceCompare(s string, t string) bool {
	for i, j := len(s)-1, len(t)-1; i >= 0 || j >= 0; i, j = i-1, j-1 {
		// * Find position of next possible char in s
		i = backspaceCompareHelper(s, i, 0)

		// * Find position of next possible char in t
		j = backspaceCompareHelper(t, j, 0)

		if ((i >= 0) != (j >= 0)) || (i >= 0 && j >= 0 && s[i] != t[j]) {
			return false
		}
	}

	return true
}

func backspaceCompareHelper(s string, pos, skip int) int {
	for pos >= 0 {
		if s[pos] == '#' {
			skip++
		} else if skip > 0 {
			skip--
		} else {
			break
		}

		pos--
	}

	return pos
}

// @lc code=end

