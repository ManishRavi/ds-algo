/*
 * @lc app=leetcode id=1480 lang=golang
 *
 * [1480] Running Sum of 1d Array
 */

// @lc code=start

// * Prefix Sum Solution | O(n) Time | O(1) Space

func runningSum(nums []int) []int {
	numsSize := len(nums)
	for i := 1; i < numsSize; i++ {
		nums[i] += nums[i-1]
	}

	return nums
}

// @lc code=end

