/*
 * @lc app=leetcode id=35 lang=golang
 *
 * [35] Search Insert Position
 */

// @lc code=start
func searchInsert(nums []int, target int) int {
	if len(nums) <= 0 {
		return 0
	}

	left, right, mid := 0, len(nums)-1, 0
	for left <= right {
		mid = left + (right-left)/2
		if nums[mid] == target {
			return mid
		} else if nums[mid] < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return left
}

// @lc code=end

