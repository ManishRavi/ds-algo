package main

func lengthOfLastWord(s string) int {
	if len(s) <= 0 {
		return 0
	}

	count := 0
	for i := len(s) - 1; i >= 0; i-- {
		if s[i] != ' ' {
			count++
		} else if count > 0 {
			return count
		}
	}

	return count
}
