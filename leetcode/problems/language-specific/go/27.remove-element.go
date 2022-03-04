/*
 * @lc app=leetcode id=27 lang=golang
 *
 * [27] Remove Element
 */

// @lc code=start
func removeElement(nums []int, val int) int {
	if len(nums) <= 0 {
		return len(nums)
	}

	i := 0
	for j := 0; j < len(nums); j += 1 {
		if nums[j] != val {
			if i != j {
				nums[i] = nums[j]
			}

			i += 1
		}
	}

	return i
}

// @lc code=end

