package main

import "strings"

func reverseWords(s string) string {
	if len(s) <= 1 {
		return s
	}

	res, sSplit := "", strings.Split(s, " ")
	for _, v1 := range sSplit {
		for i := len(v1) - 1; i >= 0; i-- {
			res += string(v1[i])
		}

		res += " "
	}

	return res[:len(res)-1]
}
