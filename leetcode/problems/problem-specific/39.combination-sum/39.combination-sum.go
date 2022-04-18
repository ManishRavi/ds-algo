package main

func combinationSum(candidates []int, target int) [][]int {
	if len(candidates) <= 0 {
		return [][]int{}
	}

	res := [][]int{}
	combinationSumHelper(candidates, target, 0, []int{}, &res)
	return res
}

func combinationSumHelper(candidates []int, target, start int, combination []int, res *[][]int) {
	if target < 0 {
		return
	}
	if target == 0 {
		*res = append(*res, append([]int{}, combination...))
		return
	}

	for i := start; i < len(candidates); i++ {
		combination = append(combination, candidates[i])
		combinationSumHelper(candidates, target-candidates[i], i, combination, res)
		combination = combination[:len(combination)-1]
	}
}
