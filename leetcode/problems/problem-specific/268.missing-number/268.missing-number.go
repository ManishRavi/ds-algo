package main

func missingNumber(nums []int) int {
	n := len(nums)
	total, sum := (n*(n+1))/2, 0
	for _, v := range nums {
		sum += v
	}

	return total - sum
}
