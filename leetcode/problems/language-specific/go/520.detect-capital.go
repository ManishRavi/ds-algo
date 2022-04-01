/*
 * @lc app=leetcode id=520 lang=golang
 *
 * [520] Detect Capital
 */

// @lc code=start
func detectCapitalUse(word string) bool {
	var isUpperCase = regexp.MustCompile(`^[A-Z]+$`).MatchString
	var isLowerCase = regexp.MustCompile(`^[a-z]+$`).MatchString
	var isTitleCase = regexp.MustCompile(`^[A-Z]{1}[a-z]+$`).MatchString

	return isUpperCase(word) || isLowerCase(word) || isTitleCase(word)
}

// @lc code=end

