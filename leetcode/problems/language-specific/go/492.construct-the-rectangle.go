/*
 * @lc app=leetcode id=492 lang=golang
 *
 * [492] Construct the Rectangle
 */

// @lc code=start
func constructRectangle(area int) []int {
	res := []int{}
	for i := int(math.Ceil(math.Sqrt(float64(area)))); i >= 0; i-- {
		if area%i == 0 {
			v1, v2 := i, int(area/i)
			res = append(res, findMax(v1, v2), findMin(v1, v2))
			return res
		}
	}

	return res
}

func findMax(a, b int) int {
	if a >= b {
		return a
	}

	return b
}

func findMin(a, b int) int {
	if a <= b {
		return a
	}

	return b
}

// @lc code=end

