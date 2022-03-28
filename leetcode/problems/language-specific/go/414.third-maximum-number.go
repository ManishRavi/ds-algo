/*
 * @lc app=leetcode id=414 lang=golang
 *
 * [414] Third Maximum Number
 */

// @lc code=start
func thirdMax(nums []int) int {
	firstMax, secondMax, thirdMax := math.MinInt64, math.MinInt64, math.MinInt64
	for _, v := range nums {
		switch {
		case v > firstMax:
			firstMax, secondMax, thirdMax = v, firstMax, secondMax
		case v > secondMax && v != firstMax:
			secondMax, thirdMax = v, secondMax
		case v > thirdMax && v != firstMax && v != secondMax:
			thirdMax = v
		}
	}

	if thirdMax != math.MinInt64 {
		return thirdMax
	}

	return firstMax
}

// @lc code=end

