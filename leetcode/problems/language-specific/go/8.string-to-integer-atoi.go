/*
 * @lc app=leetcode id=8 lang=golang
 *
 * [8] String to Integer (atoi)
 */

// @lc code=start
func myAtoi(s string) int {
	if len(s) <= 0 {
		return 0
	}

	var isDigit = regexp.MustCompile(`^[0-9]$`).MatchString
	res, sign, i, n := 0, 1, 0, len(s)
	for i < n && s[i] == ' ' {
		i++
	}
	if i >= n {
		return res
	}

	if s[i] == '+' {
		sign = 1
		i++
	} else if s[i] == '-' {
		sign = -1
		i++
	}

	for i < n && isDigit(string(s[i])) {
		res = (res * 10) + int(s[i]-'0')
		if res*sign > math.MaxInt32 {
			return math.MaxInt32
		} else if res*sign < math.MinInt32 {
			return math.MinInt32
		}

		i++
	}

	return res * sign
}

// @lc code=end

