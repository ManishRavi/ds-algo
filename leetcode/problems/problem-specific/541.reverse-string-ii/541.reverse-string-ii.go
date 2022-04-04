package main

import "strings"

func reverseStr(s string, k int) string {
	if len(s) <= 1 {
		return s
	}

	sSlice := strings.Split(s, "")
	i, j := 0, k-1
	for j < len(sSlice) {
		reverse(sSlice, i, j)
		nextIndex := i + (2 * k)
		i, j = nextIndex, nextIndex+(k-1)
	}

	if i < len(sSlice) {
		reverse(sSlice, i, len(sSlice)-1)
	}

	return strings.Join(sSlice, "")
}

func reverse(slice []string, start, end int) {
	for start < end {
		slice[start], slice[end] = slice[end], slice[start]
		start++
		end--
	}
}
