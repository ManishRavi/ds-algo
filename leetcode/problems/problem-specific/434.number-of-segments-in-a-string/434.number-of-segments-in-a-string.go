package main

func countSegments(s string) int {
	if len(s) <= 0 {
		return 0
	}

	count := 0
	for i := range s {
		if (i == 0 || s[i-1] == ' ') && s[i] != ' ' {
			count++
		}
	}

	return count
}
