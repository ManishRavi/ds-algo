package main

// * Two Pointer Solution | O(n^2) Time | O(1) Space

func longestPalindrome(s string) string {
	sSize := len(s)
	if sSize <= 1 {
		return s
	}

	res := ""
	for i := range s {
		// * Handle Odd length
		longestPalindromeHelper(s, i, i, &res)

		// * Handle Even length
		longestPalindromeHelper(s, i, i+1, &res)
	}

	return res
}

func longestPalindromeHelper(s string, left, right int, res *string) {
	sSize := len(s)
	for left >= 0 && right < sSize && s[left] == s[right] {
		curSize := right - left + 1
		if curSize > len(*res) {
			*res = s[left : right+1]
		}

		left--
		right++
	}
}
