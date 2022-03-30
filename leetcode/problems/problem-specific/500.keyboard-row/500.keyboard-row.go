package main

import "strings"

func findWords(words []string) []string {
	res := []string{}
	mappings := map[byte]int{
		'q': 1,
		'w': 1,
		'e': 1,
		'r': 1,
		't': 1,
		'y': 1,
		'u': 1,
		'i': 1,
		'o': 1,
		'p': 1,

		'a': 2,
		's': 2,
		'd': 2,
		'f': 2,
		'g': 2,
		'h': 2,
		'j': 2,
		'k': 2,
		'l': 2,

		'z': 3,
		'x': 3,
		'c': 3,
		'v': 3,
		'b': 3,
		'n': 3,
		'm': 3,
	}

	for _, v1 := range words {
		isSameRow := true
		if len(v1) > 1 {
			for j := 1; j < len(v1); j++ {
				if mappings[strings.ToLower(string(v1[j-1]))[0]] != mappings[strings.ToLower(string(v1[j]))[0]] {
					isSameRow = false
					break
				}
			}
		}

		if isSameRow {
			res = append(res, v1)
		}
	}

	return res
}
