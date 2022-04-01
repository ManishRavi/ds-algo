/*
 * @lc app=leetcode id=709 lang=golang
 *
 * [709] To Lower Case
 */

// @lc code=start
func toLowerCase(s string) string {
	res := ""
	for _, v := range s {
		if v >= 'A' && v <= 'Z' {
			res += string(v + 32)
		} else {
			res += string(v)
		}
	}

	return res
}

// @lc code=end

