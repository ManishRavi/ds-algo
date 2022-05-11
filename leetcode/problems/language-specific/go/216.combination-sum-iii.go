/*
 * @lc app=leetcode id=216 lang=golang
 *
 * [216] Combination Sum III
 */

// @lc code=start

// * Backtracking Solution | O(2^n) Time | O(k) Space

func combinationSum3(k int, n int) [][]int {
	res := [][]int{}
	if n <= 0 || k <= 0 || k > n {
		return res
	}

	combinationSum3Helper(k, n, 1, []int{}, &res)
	return res
}

func combinationSum3Helper(k, n, start int, combination []int, res *[][]int) {
	if n < 0 {
		return
	}
	if n == 0 && k == len(combination) {
		*res = append(*res, append([]int{}, combination...))
		return
	}

	for i := start; i <= 9; i++ {
		combination = append(combination, i)
		combinationSum3Helper(k, n-i, i+1, combination, res)
		combination = combination[:len(combination)-1]
	}
}

// @lc code=end

