/*
 * @lc app=leetcode id=65 lang=golang
 *
 * [65] Valid Number
 */

// @lc code=start

// * Regex Solution

func isNumber(s string) bool {
	reg, _ := regexp.Compile("^[+-]?(\\d+(\\.\\d*)?|\\.\\d+)([eE][+-]?\\d+)?$")
	return reg.MatchString(s)
}

// @lc code=end

