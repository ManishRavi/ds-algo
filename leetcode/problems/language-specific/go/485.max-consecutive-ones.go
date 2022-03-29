/*
 * @lc app=leetcode id=485 lang=golang
 *
 * [485] Max Consecutive Ones
 */

// @lc code=start
func findMaxConsecutiveOnes(nums []int) int {
	maxCount, curCount := 0, 0
	for _, v := range nums {
		if v == 1 {
			curCount++
		} else {
			curCount = 0
		}

		if curCount > maxCount {
			maxCount = curCount
		}
	}

	return maxCount
}

// @lc code=end

