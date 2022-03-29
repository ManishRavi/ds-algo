package main

import "strings"

func licenseKeyFormatting(s string, k int) string {
	res, curCount := "", 0
	for i := len(s) - 1; i >= 0; i-- {
		vString := string(s[i])
		if vString == "-" {
			continue
		}

		curCount++
		res = strings.ToUpper(vString) + res
		if curCount == k {
			curCount = 0
			res = "-" + res
		}
	}

	if len(res) > 0 && res[0] == '-' {
		return res[1:]
	}

	return res
}
