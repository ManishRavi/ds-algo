package main

func checkPerfectNumber(num int) bool {
	if num%2 != 0 {
		return false
	}

	divisorSum := 3 // (1 + 2)
	for i := 3; i <= int(num/2); i++ {
		if num%i == 0 {
			divisorSum += i
		}
	}

	return divisorSum == num
}
