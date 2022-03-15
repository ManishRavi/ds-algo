/*
 * @lc app=leetcode id=202 lang=golang
 *
 * [202] Happy Number
 */

// @lc code=start
func isHappy(n int) bool {
	slow, fast := n, n
	for {
		slow = square(slow)
		fast = square(square(fast))
		if slow == fast {
			break
		}
	}

	return slow == 1
}

func square(n int) int {
	res := 0
	for n != 0 {
		d := n % 10
		res += d * d
		n /= 10
	}

	return res
}

// @lc code=end

