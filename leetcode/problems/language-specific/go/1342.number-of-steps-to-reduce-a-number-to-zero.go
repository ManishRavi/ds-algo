/*
 * @lc app=leetcode id=1342 lang=golang
 *
 * [1342] Number of Steps to Reduce a Number to Zero
 */

// @lc code=start

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

// @lc code=end

