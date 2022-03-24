package main

import "strings"

func reverseVowels(s string) string {
	if len(s) <= 1 {
		return s
	}

	b := []byte(s)
	left, right := 0, len(b)-1
	for left < right {
		if !isVowel(b[left]) && !isVowel(b[right]) {
			left++
			right--
		} else if !isVowel(b[left]) {
			left++
		} else if !isVowel(b[right]) {
			right--
		} else {
			b[left], b[right] = b[right], b[left]
			left++
			right--
		}
	}

	return string(b)
}

func isVowel(b byte) bool {
	res := false
	switch strings.ToLower(string(b)) {
	case "a", "e", "i", "o", "u":
		res = true
	default:
		res = false
	}

	return res
}
