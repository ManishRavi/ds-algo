package main

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}

	res, n := 0, x
	for n != 0 {
		res *= 10
		res += n % 10
		n /= 10
	}

	return res == x
}
