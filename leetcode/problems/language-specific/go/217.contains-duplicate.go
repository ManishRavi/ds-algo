/*
 * @lc app=leetcode id=217 lang=golang
 *
 * [217] Contains Duplicate
 */

// @lc code=start
func containsDuplicate(nums []int) bool {
	if len(nums) <= 1 {
		return false
	}

	mappings := map[int]int{}
	for _, v := range nums {
		mappings[v]++
		if mappings[v] > 1 {
			return true
		}
	}

	return false
}

// @lc code=end

