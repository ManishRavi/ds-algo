/*
 * @lc app=leetcode id=367 lang=golang
 *
 * [367] Valid Perfect Square
 */

// @lc code=start
func isPerfectSquare(num int) bool {
	if num == 1 {
		return true
	}

	left, right := 2, int(num/2)
	for left <= right {
		mid := left + (right-left)/2
		squareVal := mid * mid
		if squareVal == num {
			return true
		} else if squareVal < num {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return false
}

// @lc code=end

func isPerfectSquareLinear(num int) bool {
	if num == 1 {
		return true
	}

	res := false
	for i := 2; i <= int(num/2); i++ {
		squareVal := i * i
		if squareVal == num {
			res = true
			break
		} else if squareVal > num {
			res = false
			break
		}
	}

	return res
}
