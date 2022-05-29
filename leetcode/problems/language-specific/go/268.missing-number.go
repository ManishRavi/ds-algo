/*
 * @lc app=leetcode id=268 lang=golang
 *
 * [268] Missing Number
 */

// @lc code=start

// * Math Solution | O(n) Time | O(1) Space

func missingNumber(nums []int) int {
	numsSize := len(nums)
	total, sum := (numsSize*(numsSize+1))/2, 0
	for _, v := range nums {
		sum += v
	}

	return total - sum
}

// @lc code=end

