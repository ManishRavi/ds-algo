/*
 * @lc app=leetcode id=125 lang=golang
 *
 * [125] Valid Palindrome
 */

// @lc code=start
func isPalindrome(s string) bool {
	if len(s) <= 1 {
		return true
	}

	var isAlphanumeric = regexp.MustCompile(`^[a-zA-Z0-9]$`).MatchString
	left, right := 0, len(s)-1
	for left < right {
		if !isAlphanumeric(string(s[left])) {
			left++
		} else if !isAlphanumeric(string(s[right])) {
			right--
		} else if strings.ToLower(string(s[left])) != strings.ToLower(string(s[right])) {
			return false
		} else {
			left++
			right--
		}

	}

	return true
}

// @lc code=end

