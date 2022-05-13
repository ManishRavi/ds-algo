package main

import "sort"

// * Backtracking Solution | O(n!) Time | O(n) Space

func permuteUnique(nums []int) [][]int {
	if len(nums) <= 0 {
		return [][]int{}
	}

	res := [][]int{}
	sort.Ints(nums)
	permuteUniqueHelper(nums, make([]bool, len(nums)), []int{}, &res)
	return res
}

func permuteUniqueHelper(nums []int, used []bool, permutation []int, res *[][]int) {
	if len(permutation) == len(nums) {
		*res = append(*res, append([]int{}, permutation...))
		return
	}

	for i := range nums {
		// * Skip duplicates
		if used[i] || (i > 0 && nums[i] == nums[i-1] && !used[i-1]) {
			continue
		}

		used[i] = true
		permutation = append(permutation, nums[i])
		permuteUniqueHelper(nums, used, permutation, res)
		permutation = permutation[:len(permutation)-1]
		used[i] = false
	}
}
