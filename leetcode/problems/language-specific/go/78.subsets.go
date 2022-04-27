/*
 * @lc app=leetcode id=78 lang=golang
 *
 * [78] Subsets
 */

// @lc code=start
func subsets(nums []int) [][]int {
	if len(nums) <= 0 {
		return [][]int{}
	}

	res := [][]int{}
	subsetsHelper(nums, 0, []int{}, &res)
	return res
}

func subsetsHelper(nums []int, start int, subset []int, res *[][]int) {
	*res = append(*res, append([]int{}, subset...))

	for i := start; i < len(nums); i++ {
		subset = append(subset, nums[i])
		subsetsHelper(nums, i+1, subset, res)
		subset = subset[:len(subset)-1]
	}
}

// @lc code=end

