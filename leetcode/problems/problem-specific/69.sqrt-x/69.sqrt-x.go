package main

func mySqrt(x int) int {
	if x == 0 || x == 1 {
		return x
	}

	left, right, res := 0, x/2, 0
	for left <= right {
		mid := left + (right-left)/2
		if mid*mid == x {
			return mid
		} else if mid*mid < x {
			left = mid + 1
			res = mid
		} else {
			right = mid - 1
		}
	}

	return res
}
