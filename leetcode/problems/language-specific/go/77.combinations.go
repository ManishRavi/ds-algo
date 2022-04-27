/*
 * @lc app=leetcode id=77 lang=golang
 *
 * [77] Combinations
 */

// @lc code=start
func combine(n int, k int) [][]int {
	if n <= 0 || k <= 0 {
		return [][]int{}
	}

	res := [][]int{}
	combineHelper(n, k, 1, []int{}, &res)
	return res
}

func combineHelper(n, k, start int, combination []int, res *[][]int) {
	if len(combination) == k {
		*res = append(*res, append([]int{}, combination...))
		return
	}

	for i := start; i <= n; i++ {
		combination = append(combination, i)
		combineHelper(n, k, i+1, combination, res)
		combination = combination[:len(combination)-1]
	}
}

// @lc code=end

