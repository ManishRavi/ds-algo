package main

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
