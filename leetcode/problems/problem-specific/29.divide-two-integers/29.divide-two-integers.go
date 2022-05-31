package main

import "math"

// * Bit Manipulation Solution | O(logn^2) Time | O(1) Space

func divide(dividend int, divisor int) int {
	if (dividend == 1<<31) && (divisor == -1) {
		return (1 << 31) - 1
	}

	isPositive := false
	if (dividend >= 0) == (divisor >= 0) {
		isPositive = true
	}

	dividend, divisor = int(math.Abs(float64(dividend))), int(math.Abs(float64(divisor)))
	res := 0
	for (dividend - divisor) >= 0 {
		count := 0
		for (dividend - (divisor << 1 << count)) >= 0 {
			count++
		}

		res += 1 << count
		dividend -= divisor << count
	}

	if !isPositive {
		res = -res
	}
	if res > (1<<31)-1 {
		res = (1 << 31) - 1
	}

	return res
}
