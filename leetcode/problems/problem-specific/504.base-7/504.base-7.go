package main

import "math"

func convertToBase7(num int) string {
	if num == 0 {
		return "0"
	}

	res, isNegativeNum := "", false
	if num < 0 {
		isNegativeNum = true
	}

	num = int(math.Abs(float64(num)))
	for num != 0 {
		res = string(48+(num%7)) + res
		num /= 7
	}

	if isNegativeNum {
		res = "-" + res
	}

	return res
}
