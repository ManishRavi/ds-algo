package main

import "regexp"

func detectCapitalUse(word string) bool {
	var isUpperCase = regexp.MustCompile(`^[A-Z]+$`).MatchString
	var isLowerCase = regexp.MustCompile(`^[a-z]+$`).MatchString
	var isTitleCase = regexp.MustCompile(`^[A-Z]{1}[a-z]+$`).MatchString

	return isUpperCase(word) || isLowerCase(word) || isTitleCase(word)
}
