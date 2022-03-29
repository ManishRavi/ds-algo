/*
 * @lc app=leetcode id=448 lang=golang
 *
 * [448] Find All Numbers Disappeared in an Array
 */

// @lc code=start
func findDisappearedNumbers(nums []int) []int {
	res, n := []int{}, len(nums)
	for i := range nums {
		nums[(nums[i]-1)%n] += n
	}
	for i := range nums {
		if nums[i] <= n {
			res = append(res, i+1)
		}
	}

	return res
}

// @lc code=end

