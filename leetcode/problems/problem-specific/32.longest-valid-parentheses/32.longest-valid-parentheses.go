package main

// * Two Pass Solution | O(n) Time | O(1) Space

func longestValidParentheses(s string) int {
	sSize := len(s)
	if sSize <= 0 {
		return 0
	}

	res, open, close := 0, 0, 0
	// * Forward Pass
	for i := 0; i < sSize; i++ {
		if s[i] == '(' {
			open++
		} else {
			close++
		}

		if open == close {
			res = findMax(res, open+close)
		} else if close > open {
			open, close = 0, 0
		}
	}

	open, close = 0, 0
	// * Backward Pass
	for i := sSize - 1; i >= 0; i-- {
		if s[i] == '(' {
			open++
		} else {
			close++
		}

		if open == close {
			res = findMax(res, open+close)
		} else if open > close {
			open, close = 0, 0
		}
	}

	return res
}

func findMax(a, b int) int {
	if a >= b {
		return a
	}

	return b
}
