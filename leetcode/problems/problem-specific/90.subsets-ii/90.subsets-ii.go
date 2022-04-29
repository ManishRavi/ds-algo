package main

import "sort"

func subsetsWithDup(nums []int) [][]int {
	if len(nums) <= 0 {
		return [][]int{}
	}

	res := [][]int{}
	sort.Ints(nums)
	subsetsWithDupHelper(nums, 0, []int{}, &res)
	return res
}

func subsetsWithDupHelper(nums []int, start int, subset []int, res *[][]int) {
	*res = append(*res, append([]int{}, subset...))

	for i := start; i < len(nums); i++ {
		if i > start && nums[i] == nums[i-1] {
			continue
		}

		subset = append(subset, nums[i])
		subsetsWithDupHelper(nums, i+1, subset, res)
		subset = subset[:len(subset)-1]
	}
}
