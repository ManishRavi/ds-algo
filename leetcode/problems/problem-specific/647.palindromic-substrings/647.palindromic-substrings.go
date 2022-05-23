package main

// * Two Pointer Solution | O(n^2) Time | O(1) Space

func countSubstrings(s string) int {
	res := 0
	for i := range s {
		// * Handle Odd length
		countSubstringsHelper(s, i, i, &res)

		// * Handle Even length
		countSubstringsHelper(s, i, i+1, &res)
	}

	return res
}

func countSubstringsHelper(s string, left, right int, res *int) {
	sSize := len(s)
	for left >= 0 && right < sSize && s[left] == s[right] {
		*res++
		left--
		right++
	}
}
