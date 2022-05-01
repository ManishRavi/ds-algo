/*
 * @lc app=leetcode id=89 lang=golang
 *
 * [89] Gray Code
 */

// @lc code=start
func grayCode(n int) []int {
	res := []int{0}
	if n == 0 {
		return res
	}

	for i := 0; i < n; i++ {
		curVal := int(math.Pow(2, float64(i)))
		for i := len(res) - 1; i >= 0; i-- {
			res = append(res, curVal+res[i])
		}
	}

	return res
}

// @lc code=end

