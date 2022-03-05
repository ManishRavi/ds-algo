package main

import "strings"

func lengthOfLastWord(s string) int {
	if len(s) <= 0 {
		return 0
	}

	count := 0
	s = strings.Trim(s, " ")
	for i := len(s) - 1; i >= 0; i-- {
		if s[i] == ' ' {
			break
		}
		count++
	}

	return count
}
