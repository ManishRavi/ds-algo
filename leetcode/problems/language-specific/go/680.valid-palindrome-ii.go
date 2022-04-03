/*
 * @lc app=leetcode id=680 lang=golang
 *
 * [680] Valid Palindrome II
 */

// @lc code=start
func validPalindrome(s string) bool {
	i, j := 0, len(s)-1
	for i < j {
		if s[i] != s[j] {
			return validPalindromeHelper(s, i+1, j) || validPalindromeHelper(s, i, j-1)
		}

		i++
		j--
	}

	return true
}

func validPalindromeHelper(s string, i, j int) bool {
	for i < j {
		if s[i] != s[j] {
			return false
		}

		i++
		j--
	}

	return true
}

// @lc code=end

