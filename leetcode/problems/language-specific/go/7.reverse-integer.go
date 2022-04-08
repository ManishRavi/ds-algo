/*
 * @lc app=leetcode id=7 lang=golang
 *
 * [7] Reverse Integer
 */

// @lc code=start
func reverse(x int) int {
	res, n := 0, int(math.Abs(float64(x)))
	for n != 0 {
		res *= 10
		res += n % 10
		n /= 10
	}

	if x < 0 {
		res = -res
	}
	if res < math.MinInt32 || res > math.MaxInt32 {
		return 0
	}

	return res
}

// @lc code=end

