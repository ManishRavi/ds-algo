/*
 * @lc app=leetcode id=40 lang=golang
 *
 * [40] Combination Sum II
 */

// @lc code=start
func combinationSum2(candidates []int, target int) [][]int {
	if len(candidates) <= 0 {
		return [][]int{}
	}

	res := [][]int{}
	sort.Ints(candidates)
	combinationSum2Helper(candidates, target, 0, []int{}, &res)
	return res
}

func combinationSum2Helper(candidates []int, target, start int, combination []int, res *[][]int) {
	if target < 0 {
		return
	}
	if target == 0 {
		*res = append(*res, append([]int{}, combination...))
		return
	}

	for i := start; i < len(candidates); i++ {
		if i > start && candidates[i] == candidates[i-1] {
			continue
		}

		combination = append(combination, candidates[i])
		combinationSum2Helper(candidates, target-candidates[i], i+1, combination, res)
		combination = combination[:len(combination)-1]
	}
}

// @lc code=end

