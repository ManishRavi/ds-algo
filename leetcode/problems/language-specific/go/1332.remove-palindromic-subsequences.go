/*
 * @lc app=leetcode id=1332 lang=golang
 *
 * [1332] Remove Palindromic Subsequences
 */

// @lc code=start

// * Two Pointer Solution | O(n) Time | O(1) Space

func removePalindromeSub(s string) int {
	if isPalindrome(s) {
		return 1
	}

	return 2
}

func isPalindrome(s string) bool {
	left, right := 0, len(s)-1
	for left <= right {
		if s[left] != s[right] {
			return false
		}

		left++
		right--
	}

	return true
}

// @lc code=end

