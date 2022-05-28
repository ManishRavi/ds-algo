package main

// * Iterative Solution | O(n) Time | O(1) Space

func numberOfSteps(num int) int {
	stepCounter := 0
	for num != 0 {
		stepCounter++
		if isEvenDigit(num) {
			num /= 2
		} else {
			num -= 1
		}
	}

	return stepCounter
}

func isEvenDigit(num int) bool {
	if num%2 == 0 {
		return true
	}

	return false
}
