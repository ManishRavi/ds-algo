package main

func permute(nums []int) [][]int {
	if len(nums) <= 0 {
		return [][]int{}
	}

	res := [][]int{}
	permuteHelper(nums, make([]bool, len(nums)), []int{}, &res)
	return res
}

func permuteHelper(nums []int, used []bool, permutation []int, res *[][]int) {
	if len(permutation) == len(nums) {
		*res = append(*res, append([]int{}, permutation...))
		return
	}

	for i := range nums {
		if used[i] {
			continue
		}

		used[i] = true
		permutation = append(permutation, nums[i])
		permuteHelper(nums, used, permutation, res)
		permutation = permutation[:len(permutation)-1]
		used[i] = false
	}
}
