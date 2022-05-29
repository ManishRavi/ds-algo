package main

// * Math Solution | O(n) Time | O(1) Space

func missingNumber(nums []int) int {
	numsSize := len(nums)
	total, sum := (numsSize*(numsSize+1))/2, 0
	for _, v := range nums {
		sum += v
	}

	return total - sum
}
