/*
 * @lc app=leetcode id=495 lang=golang
 *
 * [495] Teemo Attacking
 */

// @lc code=start
func findPoisonedDuration(timeSeries []int, duration int) int {
	if len(timeSeries) <= 0 || duration == 0 {
		return 0
	}

	// * Initialze res with duration to accomodate last element/attack
	res := duration
	for i := 0; i < len(timeSeries)-1; i++ {
		res += findMin(duration, timeSeries[i+1]-timeSeries[i])
	}

	return res
}

func findMin(a, b int) int {
	if a <= b {
		return a
	}

	return b
}

// @lc code=end

