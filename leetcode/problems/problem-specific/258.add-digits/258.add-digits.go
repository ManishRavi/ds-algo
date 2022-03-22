package main

func addDigits(num int) int {
	if num == 0 {
		return num
	}

	return ((num - 1) % 9) + 1
}
