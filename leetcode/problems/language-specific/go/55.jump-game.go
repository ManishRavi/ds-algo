/*
 * @lc app=leetcode id=55 lang=golang
 *
 * [55] Jump Game
 */

// @lc code=start
func canJump(nums []int) bool {
	if len(nums) <= 1 {
		return true
	}

	curFarthest, n := 0, len(nums)
	for i := range nums {
		if i > curFarthest || curFarthest >= n-1 {
			break
		}

		curFarthest = findMax(curFarthest, i+nums[i])
	}

	if curFarthest >= n-1 {
		return true
	}

	return false
}

func findMax(a, b int) int {
	if a >= b {
		return a
	}

	return b
}

// @lc code=end

